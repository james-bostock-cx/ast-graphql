from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

from CheckmarxPythonSDK.CxAST import applicationsAPI, projectsAPI, scansAPI

type_defs = gql("""
type Application {
  id: String!
  name: String!
  projects: [Project!]!
}

type Project {
  id: String!
  name: String!
  applications: [Application!]
  scans: [Scan!]
  groups: [String!]!
  repoUrl: String
  mainBranch: String
  origin: String!
  createdAt: String!
}

type Scan {
  id: String!
  createdAt: String!
  initiator: String!
  projectId: String!
  branch: String!
}

type Query {
  application(id: String!): Application
  applications: [Application!]!
  project(id: String!): Project
  projects: [Project!]!
  scan(id: String!): Scan
  scans: [Scan!]!
}

schema {
  query: Query
}
""")

query = QueryType()

@query.field("application")
def resolve_application(*_, id):
    return applicationsAPI.get_an_application_by_id(id)

@query.field("applications")
def resolve_applications(_, info):
    return applicationsAPI.get_a_list_of_applications().applications

@query.field("project")
def resolve_project(*_, id):
    return projectsAPI.get_a_project_by_id(id)

@query.field("projects")
def resolve_projects(_, info):
    return projectsAPI.get_a_list_of_projects().projects

@query.field("scan")
def resolve_scan(*_, id):
    return scansAPI.get_scan_by_id(id)

@query.field("scans")
def resolve_scans(_, info):
    return scansAPI.get_a_list_of_scan().scans

application = ObjectType("Application")

project = ObjectType("Project")

@project.field("scans")
def resolve_project_scans(obj, info):
    return scansAPI.get_a_list_of_scan(project_id=obj.id).scans

scan = ObjectType("Scan")

schema = make_executable_schema(type_defs, query, application, project, scan)
app = GraphQL(schema, debug=True)
