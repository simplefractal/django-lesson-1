# Objectives
Students will be able to 

- create nested serializers
- optimize endpoints by reducing number of queries
- create management commands

# Agenda
1. [10] Walk through code-base
2. [5] Management commands
3. [15] Exercise: Create dummy data using management command
4. [30] Optimizing the endpoint
5. [10] Open Q & A, Feedback

# Warm Up Exercise
1. Create an app called `project`
2. Create a model within that app called `Project` with the following fields: `name` (CharField), `client` (ForeignKey)
3. Create a serialize called `ProjectSerializer` that returns the name and the client (just the id will be the default) and expose it a GET endpoint. 

# Create a nested serializer
1. Now let's nest a `Client Serializer` underneath the `ProjectSerializer`.
2. Let's also add a M2M on `Project` called `members` and add a corresponding `Account` model that FKs to `tag`.
3. Let's create the `MembersSerializer` that makes use of `TagSerializer` and ensure this is all exposed in the endpoint.

# Django Management Commands
Let's create a dummy management command.

# Exercise: Create dummy data using management commands.
- Create 300 projects
- Create 10 members
- Create 15 clients
- Create 20 TaskTags, of which one is "Urgent" 

For each project, randomly assign 3 members and randomly pick a client.

For each client, create 5 tasks and randomly assign 1-3 tasktags to each task.

# Measuring # of queries
Let's use `django-querycount`.

# Optimization
Let's create our serialization by hand for a more efficient solution.

# Q & A
Thoughts? Questions? Comments?
