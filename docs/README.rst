ploneintranet.workspace
=======================

* `Documentation @ RTD <http://ploneintranetworkspace.readthedocs.org>`_
* `Source code @ GitHub <http://github.com/ploneintranet/ploneintranet.workspace>`_
* `Continuous Integration @ Travis CI <http://travis-ci.org/ploneintranet/ploneintranet.workspace>`_
* `Code Coverage @ Coveralls.io <http://coveralls.io/r/ploneintranet/ploneintranet.workspace>`_

Summary
=======

This package provides a Workspace container that can be used as a
project space, team space or community space.

At it's core, it's a Dexterity Container with
`collective.workspace <https://github.com/collective/collective.workspace>`_
behavior applied.

On top of that, it provides a policy abstraction and user interface that
enables intuitive management of security settings without having to
access, and understand, the sharing tab in Plone. The sharing tab and
functionality is retained as "advanced" settings to enable per-user
exceptions to the default security settings.

Current Status
=======

With this package installed, you get a dexterity content type 'workspace',
which has the collective.workspace behaviour applied. This will enable
the 'roster' tab, which will enable an admin to add members and workspace
admins to the workspace.

Any content added to the workspace will have the ploneintranet content
workflow applied, that will apply further restrictions on which users
can access content within your workspace. These can be adjusted via
the policy tab.

TODO
=======

* The ability to invite users to workspaces
