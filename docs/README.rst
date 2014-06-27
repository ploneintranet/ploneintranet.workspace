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

Installation
============

* Add ploneintranet.workspace to your eggs and re-buildout
* Activate the 'Plone Intranet: Workspace' add-on

Usage
=====

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
can access content within your workspace. These can be adjusted via
the policy tab.
