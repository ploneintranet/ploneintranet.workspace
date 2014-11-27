=======================
ploneintranet.workspace
=======================

.. image:: https://travis-ci.org/ploneintranet/ploneintranet.workspace.svg?branch=master
    :target: https://travis-ci.org/ploneintranet/ploneintranet.workspace
.. image:: https://coveralls.io/repos/ploneintranet/ploneintranet.workspace/badge.png?branch=master
  :target: https://coveralls.io/r/ploneintranet/ploneintranet.workspace?branch=master

* `Documentation @ RTD <http://ploneintranetworkspace.readthedocs.org>`_
* `Source code @ GitHub <http://github.com/ploneintranet/ploneintranet.workspace>`_
* `Continuous Integration @ Travis CI <http://travis-ci.org/ploneintranet/ploneintranet.workspace>`_
* `Code Coverage @ Coveralls.io <http://coveralls.io/r/ploneintranet/ploneintranet.workspace>`_

Summary
=======

This package provides a 'workspace' container and content workflow working in conjunction to provide flexible levels of content access in a Plone site.

It aims to provide a flexible team/community workspace solution, allowing teams of users to communicate and collaborate effectively within their own area of an intranet. Plone's extensive permissions are distilled into a set of distinct policies that control who can access a workspace, who can join a workspace, and what users can do once they are part of a workspace.

Installation
============

* Add ploneintranet.workspace to your eggs and re-buildout
* Activate the 'Plone Intranet: Workspace' add-on

Basic Usage
===========

With this package installed, you get a dexterity content type 'workspace',
which has the collective.workspace behaviour applied. This will enable
the 'roster' and 'policies' tabs.

The policies tab allows the creator and other workspace admins to set the
external visibility, joining and participant policies for the workspace. These
govern the openness of the workspace in terms of how free intranet users are to
join and add content.

The roster tab lists all the current members of the workspace and allows users
to add or invite new members depending on the current join policy. It also
allows admins to delegate management of the workspace to other members by
making them a 'workspace admin'

Any content added to the workspace will have the ploneintranet content
workflow applied, that will apply further restrictions on which users
can access content within your workspace. 


Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all 
copyrights on the code you contribute, to the `Plone Foundation`_, 
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
