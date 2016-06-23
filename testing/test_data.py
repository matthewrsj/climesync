import commands


class TestData():

    def __init__(self, command, mocked_input, expected_response, admin):
        self.command = command
        self.mocked_input = mocked_input
        self.expected_response = expected_response
        self.admin = admin


create_time_data = TestData(
        command=commands.create_time,
        mocked_input=[
            "1h0m", # Duration
            "p_foo", # Project slug
            ["planning", "code"], # Activity slugs
            "2016-05-04", # Date worked
            "https://www.github.com/osuosl/projectfoo/issues/42", # Issue URI
            "Worked on coding" # Notes
        ],
        expected_response={
            "created_at": "2015-05-23",
            "updated_at": None,
            "deleted_at": None,
            "uuid": "838853e3-3635-4076-a26f-7efr4e60981f",
            "revision": 1,
            "duration": 3600,
            "project": "p_foo",
            "activities": ["planning", "code"],
            "date_worked": "2016-05-04",
            "user": "test",
            "notes": "Worked on coding",
            "issue_uri": "https://www.github.com/osuosl/projectfoo/issues/42" 
        },
        admin=False)

update_time_data = TestData(
        command=commands.update_time,
        mocked_input=[
            "838853e3-3635-4076-a26f-7efr4e60981f", # UUID of time to update
            "2h0m", # Updated duration
            "p_bar", # Updated project slug
            "usertwo", # Updated user
            ["docs"], # Updated activity slugs
            "2016-06-20", # Updated date worked
            "https://www.github.com/osuosl/projectbar/issues/20", # Updated URI
            "Worked on documentation" # Updated notes
        ],
        expected_response={
            "created_at": "2014-06-12",
            "updated_at": "2015-10-18",
            "deleted_at": None,
            "uuid": "838853e3-3635-4076-a26f-7efr4e60981f",
            "revision": 2,
            "duration": 7200,
            "project": "p_bar",
            "activities": ["docs"],
            "date_worked": "2016-06-20",
            "user": "usertwo",
            "notes": "Worked on documentation",
            "issue_uri": "https://www.github.com/osuosl/projectbar/issues/20"
        },
        admin=False)

get_times_no_uuid_data = TestData(
        command=commands.get_times,
        mocked_input=[None]*8,
        expected_response=[{
            "created_at": "2014-04-17",
            "updated_at": None,
            "deleted_at": None,
            "uuid": "c3706e79-1c9a-4765-8d7f-89b4544cad56",
            "revision": 1,
            "duration": "0h0m",
            "project": ["ganeti-webmgr", "gwm"],
            "activities": ["docs", "planning"],
            "date_worked": "2014-04-17",
            "user": "userone",
            "notes": "Worked on documentation.",
            "issue_uri": "https://github.com/osuosl/ganeti_webmgr"
        },
        {
            "created_at": "2014-04-17",
            "updated_at": None,
            "deleted_at": None,
            "uuid": "12345676-1c9a-rrrr-bbbb-89b4544cad56",
            "revision": 1,
            "duration": "0h0m",
            "project": ["ganeti-webmgr", "gwm"],
            "activities": ["code", "planning"],
            "date_worked": "2014-04-17",
            "user": "usertwo",
            "notes": "Worked on coding",
            "issue_uri": "https://github.com/osuosl/ganeti_webmgr"
        },
        {
            "created_at": "2014-04-17",
            "updated_at": None,
            "deleted_at": None,
            "uuid": "12345676-1c9a-ssss-cccc-89b4544cad56",
            "revision": 1,
            "duration": "0h0m",
            "project": ["timesync", "ts"],
            "activities": ["code"],
            "date_worked": "2014-04-17",
            "user": "userthree",
            "notes": "Worked on coding",
            "issue_uri": "https://github.com/osuosl/timesync"
        }],
        admin=False)

get_times_uuid_data = TestData(
        command=commands.get_times,
        mocked_input=[
            "userone", # User
            ["gwm"], # Project slugs
            ["docs"], # Activity slugs
            "2014-04-16", # Start date
            "2014-04-18", # End date
            False, # Include revisions
            False, # Include deleted
            "838853e3-3635-4076-a26f-7efr4e60981f" # UUID
        ],
        expected_response=[{
            "created_at": "2014-04-17",
            "updated_at": None,
            "deleted_at": None,
            "uuid": "838853e3-3635-4076-a26f-7efr4e60981f",
            "revision": 1,
            "duration": "0h0m",
            "project": ["ganeti-webmgr", "gwm"],
            "activities": ["docs", "planning"],
            "date_worked": "2014-04-17",
            "user": "userone",
            "notes": "Worked on documentation.",
            "issue_uri": "https://github.com/osuosl/ganeti_webmgr"
        }],
        admin=False)

sum_times_data = TestData(
        command=commands.sum_times,
        mocked_input=[
            ["gwm"], # Project slugs
            "", # Include revisions
            "" # Include deleted
        ],
        expected_response=[],
        admin=False)

delete_time_no_data = TestData(
        command=commands.delete_time,
        mocked_input=[
            "838853e3-3635-4076-a26f-7efr4e60981f", # UUID
            False # Really?
        ],
        expected_response=[],
        admin=False)

delete_time_data = TestData(
        command=commands.delete_time,
        mocked_input=[
            "838853e3-3635-4076-a26f-7efr4e60981f", # UUID
            True # Really?
        ],
        expected_response=[{
            "status": 200
        }],
        admin=False)

create_project_data = TestData(
        command=commands.create_project,
        mocked_input=[
            "projectx", # Project name
            ["projx", "px"], # Project slugs
            "https://www.github.com/osuosl/projectx", # Project URI
            ["userone", "usertwo"], # Project users
            "code" # Default activity
        ],
        expected_response={
            "created_at": "2015-05-23",
            "updated_at": None,
            "deleted_at": None,
            "revision": 1,
            "uuid": "309eae69-21dc-4538-9fdc-e6892a9c4dd4",
            "name": "projectx",
            "slugs": ["projx", "px"],
            "uri": "https://www.github.com/osuosl/projectx",
            "users": {
                "userone": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "usertwo": {
                    "member": True,
                    "spectator": True,
                    "manager": True
                }
            },
            "default_activity": "code"
        },
        admin=True)

update_project_data = TestData(
        command=commands.update_project,
        mocked_input=[
            "projx", # Slug of project to update
            "Project X", # Updated name
            ["px"], # Updated slugs
            "https://www.github.com/osuosl/projectx", # Updated URI
            ["userone", "usertwo", "userthree"], # Updated users
            "planning" # Updated default activity
        ],
        expected_response={
            "created_at": "2015-05-23",
            "updated_at": None,
            "deleted_at": None,
            "revision": 2,
            "uuid": "309eae69-21dc-4538-9fdc-e6892a9c4dd4",
            "name": "Project X",
            "slugs": ["px"],
            "uri": "https://www.github.com/osuosl/projectx",
            "users": {
                "userone": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "usertwo": {
                    "member": True,
                    "spectator": True,
                    "manager": True
                },
                "userthree": {
                    "member": False,
                    "spectator": True,
                    "manager": False
                }
            },
            "default_activity": "planning"

        },
        admin=True)

get_projects_no_slug_data = TestData(
        command=commands.get_projects,
        mocked_input=[
            False, # Include revisions
            False, # Include deleted
            "" # Project slug
        ],
        expected_response = [{
            "created_at": "2014-07-17",
            "updated_at": "2014-07-20",
            "deleted_at": None,
            "revision": 4,
            "uuid": "a034806c-00db-4fe1-8de8-514575f31bfb",
            "name": "Ganeti Web Manager",
            "slugs": ["gwm"],
            "uri": "https://code.osuosl.org/projects/ganeti-webmgr",
            "users": {
                "patcht": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "tschuy": {
                    "member": True,
                    "spectator": True,
                    "manager": True
                }
            }
        },
        {
            "created_at": "2014-07-17",
            "updated_at": "2014-07-20",
            "deleted_at": None,
            "revision": 2,
            "uuid": "a034806c-rrrr-bbbb-8de8-514575f31bfb",
            "name": "TimeSync",
            "slugs": ["timesync", "ts"],
            "uri": "https://code.osuosl.org/projects/timesync",
            "users": {
                "patcht": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "mrsj": {
                    "member": True,
                    "spectator": True,
                    "manager": False
                },
                "tschuy": {
                    "member": True,
                    "spectator": True,
                    "manager": True
                }
            }
        },
        {
            "created_at": "2014-07-17",
            "updated_at": "2014-07-20",
            "deleted_at": None,
            "revision": 1,
            "uuid": "a034806c-ssss-cccc-8de8-514575f31bfb",
            "name": "pymesync",
            "slugs": ["pymesync", "ps"],
            "uri": "https://code.osuosl.org/projects/pymesync",
            "users": {
                "patcht": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "tschuy": {
                    "member": True,
                    "spectator": True,
                    "manager": False
                },
                "mrsj": {
                    "member": True,
                    "spectator": True,
                    "manager": True
                },
                "MaraJade": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "thai": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                }
            }
        }],
        admin=False)

get_projects_slug_data = TestData(
        command=commands.get_projects,
        mocked_input=[
            "", # Include revisions
            "", # Include deleted
            "gwm" # Project slug
        ],
        expected_response=[{
            "created_at": "2014-07-17",
            "updated_at": "2014-07-20",
            "deleted_at": None,
            "revision": 4,
            "uuid": "",
            "name": "Ganeti Web Manager",
            "slugs": ["gwm"],
            "uri": "https://code.osuosl.org/projects/ganeti-webmgr",
            "users": {
                "patcht": {
                    "member": True,
                    "spectator": False,
                    "manager": False
                },
                "tschuy": {
                    "member": True,
                    "spectator": True,
                    "manager": True
                }
            }
        }],
        admin=False)

delete_project_no_data = TestData(
        command=commands.delete_project,
        mocked_input=[
            "slug", # Project slug
            False # Really?
        ],
        expected_response=[],
        admin=True)

delete_project_data = TestData(
        command=commands.delete_project,
        mocked_input=[
            "slug", # Project slug
            True # Really?
        ],
        expected_response=[{
            "status": 200
        }],
        admin=True)
