from Acquisition._Acquisition import aq_parent
from plone.memoize.view import memoize
from zope.interface import Interface
from zope.interface import implementer
from zope.component import getMultiAdapter
from plone import api
from plone.tiles import Tile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.navigation.navtree import buildFolderTree
from plone.app.layout.navigation.interfaces import INavtreeStrategy
from Products.CMFPlone.browser.navtree import SitemapQueryBuilder
from ploneintranet.workspace.workspacefolder import IWorkspaceFolder


class INavigationTile(Interface):
    """Marker interface for the navigation tile
    """


class WorkspaceQueryBuilder(SitemapQueryBuilder):

    def __init__(self, context, root):
        super(WorkspaceQueryBuilder, self).__init__(context)
        if 'path' in self.query:
            self.query['path']['query'] = '/'.join(root.getPhysicalPath())
            if 'navtree' in self.query:
                del self.query['navtree']
            if 'navtree_start' in self.query:
                del self.query['navtree_start']
            self.query['path']['depth'] = 1


@implementer(INavigationTile)
class NavigationTile(Tile):

    index = ViewPageTemplateFile('templates/navigation.pt')

    def items(self):
        queryBuilder = WorkspaceQueryBuilder(self.context, self.root)
        strategy = getMultiAdapter((self.context, None), INavtreeStrategy)
        strategy.showAllParents = False
        strategy.rootPath = '/'.join(self.root.getPhysicalPath())

        tree = buildFolderTree(
            self.context,
            obj=self.context,
            query=queryBuilder(),
            strategy=strategy
        )
        return tree['children']

    def render(self):
        return self.index()

    def __call__(self):
        # TODO: use transient tiles with schema and data manager here
        root = self.request.form.get('root')
        if root:
            self.root = api.content.get(UID=root)
        else:
            self.root = self.context
        return self.render()

    @memoize
    def _parent(self):
        return aq_parent(self.root)

    def current_node_is_root(self):
        """
        Is the current node the root of the workspace?
        """
        return IWorkspaceFolder.providedBy(self.root)

    def parent_title(self):
        return self._parent().Title()

    def non_folderish_item_uids(self):
        # TODO: Better way of determining folderish?
        return [x['UID'] for x in self.items() if x['portal_type'] is not 'Folder']

    def folderish_item_uids(self):
        # TODO: Better way of determining folderish?
        return [x['UID'] for x in self.items() if x['portal_type'] is 'Folder']

    def any_item(self):
        """
        For data-pat-depends condition, is any item selected
        """
        return ' or '.join([x['UID'] for x in self.items()])

    def only_non_folderish(self):
        """
        For data-pat-depends condition, are only non folderish items checked
        """
        return '(%s) and not (%s)' % (
            ' or '.join(self.non_folderish_item_uids()),
            ' or '.join(self.folderish_item_uids())
        )