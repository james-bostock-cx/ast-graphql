This is a proof of concept minimal GraphQL layer on top of the CxAST
REST API.

The [Checkmarx Python
SDK](https://github.com/checkmarx-ts/checkmarx-python-sdk) is used to
access the CxAST REST API.

# Development

The [Poetry](https://https://python-poetry.org/) packaging and
dependency manager is used. After cloning the repository, a shell in a
virtual environment can be created with:

```
$ poetry shell
```

To start the server:

```
$ uvicorn ast-graphql.py
```

# Sample Queries

Get the ids, names, and scan ids of all projects:

```
{
  projects {
    id
    name
    scans {
      id
    }
  }
}
```

Get the id, name and scan ids of a specific project:

```
{
  project(id: "14fe193f-2d66-4399-9730-071c03d36948") {
    id
    name
    scans {
      id
    }
  }
}
```
