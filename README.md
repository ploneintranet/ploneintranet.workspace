[![Build Status](https://api.travis-ci.org/ploneintranet/ploneintranet.workspace.png)](https://travis-ci.org/ploneintranet/ploneintranet.workspace)

ploneintranet.workspace
=======================

This package provides a Workspace container that can be used as a project space,
team space or community space. 

At it's core, it's a Dexterity Container with collective.workspace behavior
applied.

On top of that, it provides a policy abstraction and user interface that
enables intuitive management of security settings without having to
access, and understand, the sharing tab in Plone. The sharing tab
and functionality is retained as "advanced" settings to enable
per-user exceptions to the default security settings.

We spent some care in devising a terminology to precisely express
the reasoning for all of this. Think of it as a domain-specific language.
These terms will be capitalized below.


Personas
--------

- Guest: a site user who is not a Participant in the Workspace.
- Participant: a site user with local permissions in the Workspace.
- Workspace Admin: manages users and the Workspace.
- Site Admin: manages users and permissions on the Plone site.


Policies
========

We've created screen mocks (see ./doc/) for a streamlined policy management
interface on the Workspace. This was carefully designed to be implementable
using Plone security primitives, see further below.

We envision that the policy options detailed below may be combined into
policy packages that provide some sensible scenarios out of the box.
Examples would be:

- Community = Open + Self-managed + Publishers
- Division  = Open + Admin-managed + Consumers
- Team      = Private + Team-managed + Publishers

Integrators can easily create additional combinations to target scenarios
like a HR area or a secret project. Such pre-packaged policy combinations
may be exposed to users in the form of custom content types that "under the
hood" are all just ploneintranet.workspace.

There's 3 main dimensions for the default Workspace policy, each ranging
across a scale from high security to high interactivity:


External Visibility
-------------------

External Visibility configures the permissions on the Workspace
for Guests, i.e. users who are not Participants in the Workspace.

* Secret

Secret Workspaces cannot be seen or accessed by Guests.
Only Participants can see and access a Secret Workspace.

* Private

Private Workspaces can be seen, but not be accessed by Guests.
Participants can see and access Private Workspaces.

* Open

Open Workspaces can be seen and accessed by Guests.
However Guests can only see, not respond to content in the Workspace.
Participants on the other hand can not only see and access
the Workspace but also interact with it's content.

See detailed security notes below for implementation hints.


Joining
-------

Joining configures who can add users to the Workspace.
Removing users is always reserved to Workspace Admins.

* Admin-managed

Only Workspace Admins may promote users to Participants.

* Team-managed

Existing Participants may promote users to Participants.

* Self-managed

Any user can self-join the Workspace and become a Participant.

In addition to this Workspace-level configuration, there will
be a site-level policy which determines whether non-users
(e.g. external consultants) may be created as a user in the site.
Such site-level user management may use a email domain whitelist
or new user workflowing moderation; that is out of the scope
of the Workspace.

The upshot of this is, that even an Open Self-managed Workspace will
be protected by site-level security constraints.


Participation
-------------

The Participation config determines the local permissions Participants
will have within the Workspace. Note that normal Plone roles are
orthogonal: Reader, Contributor, Reviewer and Editor do not overlap
and the same goes for the corresponding groups Readers, Contributors,
Reviewers and Editors.

We've devised the following local groups in such a way that they
combine normal Plone roles in what we think is an intuitive progression.

* Consumer   = Readers (+ extra interactive permissions)
* Producer   = Readers + Contributors
* Publisher  = Readers + Contributors + SelfPublishers
* Moderator  = Readers + Contributors + Reviewers + Editors

As you noticed, this introduces a new role SelfPublisher which allows
a user to publish their own content. This is neccessary because one wants
to be able to allow users to publish their own content without becoming
Reviewer of all the content in the Workspace.

Participation policy is stored by creating a local Participants Meta-Group
for a Workspace, and then adding this Participants Meta-Group to the right
local groups that map to the intended role assignments. For example the
policy choice Publisher would make Participants member of the groups
Readers + Contributors + SelfPublishers.


Participant Exceptions
----------------------

While this is all very nice and powerful, there will always be a need
to make exceptions. These can be made by linking to the existing sharing
tab as 'advanced policy configuration' and setting per-user rights there.

It then makes sense to also have an audit viewlet that shows you which
Participants have security settings that do not conform to the default
policy configuration.


Permissions, Roles, Groups and Meta-Groups, oh my
=================================================

Like a delicious wedding cake, the security settings are stacked in a
layered architecture. This makes it possible to have a simplified
configuration management interface frontent and at the same time have a
performant and extremely fine-grained security mechanism in the back-end.

* Permissions are the basic building block of Plone's security.
  For example: Add Content, Reply to Discussion.

* Roles are combinations of Permissions that make sense as a group.
  For example: Reader = View Content + View Folder Contents.

* Groups map Roles to users.
  For example: All users in group Readers get role Reader.

* Meta Groups map Roles to Groups.
  For example: All Participants are in the group Publisher.

There's some details and intricacies here that are worth highlighting.

First of all, why have a group Readers when you can directly map a user to the
role Reader? Doing a local role assignment for a user in the context of a
Workspace requires a costly reindex of the Workspace and recursively of all
content contained in that Workspace. Assigning role Reader to the group
Readers makes this reindex a one-time event. After that, users can be
added to the group Readers without requiring a reindex.

As a consequence, a Workspace has local groups for Reader, Contributor,
Reviewer and Editor. Additionally, a workspace has a local Meta-Group
for Participants. Each of these local groups are of course created separately
for each Workspace.

Why have a Meta-Group Participants when you can directly assign users
to the groups Reader, Contributor etc? This brings 2 benefits:

- The group Participants manages the default policy for the Workspace. 
  All exceptions to the default policy are made as assignments of users
  to other local groups via the advanced sharing facility. That way you
  can keep track of exceptions.

Suppose you did not do this and assigned users directly to local groups.
Say the you'd want to add users to Readers + Contributors by default.
Then you'd make an exception for Barney the Boss by adding him to
Reviewers + Editors as well. If you then change the default policy
to Readers + Contributors + Reviewers + Editors you'd have to add 
all others to those groups as well. If then you change your mind
and want to revert the default policy back to only Readers + Contributors,
you'd have no way to know that you'd need to demote all uses except
Barney the Boss - you would demote Barney as well. Not good.

- Secondly, having a separate Meta-Group Participants allows you to
  add extra permissions and roles that are not implied by the normal
  group assignments.

Specifically, in an Open Workspace Guests have the Reader role by
virtue of acquiring the global Readers group. Since the Readers
group is acquired, we cannot redefine it's permissions locally.
However we want to grant Participants at minimal Consumer permissions,
which in addition to Reader include various social interactivity
permissions like Add Discussion Item, Create Plonesocial StatusUpdate etc.


Consistency
-----------

We've audited the settings architecture described above for possible
inconsistent settings. These should be caught by some Javascript logic 
in the configuration policy view.

- A Secret Workspace cannot be Self-managed

Additionally, the implementation needs to take care of the following:

- Only Open Workspaces acquire global Readers group and Reader permission.

In all other cases, acquisition of Readers should be disabled.
For Contributors, Reviewers and Editors acquisition should be disabled always.

