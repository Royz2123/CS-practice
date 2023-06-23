from copy import deepcopy
from typing import Any, Dict

from code_editor import code_editor

EDITOR_BUTTONS = [
    {
        "name": "Copy",
        "feather": "Copy",
        "hasText": True,
        "alwaysOn": True,
        "commands": [
            "copyAll",
            [
                "infoMessage",
                {
                    "text": "Copied to clipboard!",
                    "timeout": 2500,
                    "classToggle": "show"
                }
            ]
        ],
        "style": {"right": "0.4rem"}
    },
    {
        "name": "Run",
        "feather": "Play",
        "primary": True,
        "hasText": True,
        "alwaysOn": True,
        "showWithIcon": True,
        "commands": [
            "submit",
            [
                "infoMessage",
                {
                    "text": "Running...",
                    "timeout": 2500,
                    "classToggle": "show"
                }
            ]
        ],
        "style": {
            "bottom": "0.44rem",
            "right": "0.4rem"
        }
    },
    {
        "name": "Test",
        "feather": "Play",
        "primary": True,
        "hasText": True,
        "alwaysOn": True,
        "showWithIcon": True,
        "commands": [
            [
                "response",
                "test"
            ],
            [
                "infoMessage",
                {
                    "text": "Testing...",
                    "timeout": 2500,
                    "classToggle": "show"
                }
            ]
        ],
        "style": {
            "bottom": "2.00rem",
            "right": "0.4rem"
        }
    }
]

EDITOR_CSS = '''
    background-color: #bee1e5;

    body > #root .ace-streamlit-dark~& {
       background-color: #262830;
    }

    .ace-streamlit-dark~& span {
       color: #fff;
       opacity: 0.6;
    }

    span {
       color: #000;
       opacity: 0.5;
    }

    .code_editor-info.message {
       width: inherit;
       margin-right: 75px;
       order: 2;
       text-align: center;
       opacity: 0;
       transition: opacity 0.7s ease-out;
    }

    .code_editor-info.message.show {
       opacity: 0.6;
    }

    .ace-streamlit-dark~& .code_editor-info.message.show {
       opacity: 0.5;
    }
    '''

EDITOR_INFO_BAR = {
    "name": "language info",
    "css": EDITOR_CSS,
    "style": {
        "order": "1",
        "display": "flex",
        "flexDirection": "row",
        "alignItems": "center",
        "width": "100%",
        "height": "2.5rem",
        "padding": "0rem 0.75rem",
        "borderRadius": "8px 8px 0px 0px",
        "zIndex": "9993"
    },
    "info": [{
        "name": "Java",
        "style": {"width": "300px"}
    }]
}

DEFAULT_INITIAL_CODE = "print('hello world')\n\n\n"


def write_editor(initial_code: str = DEFAULT_INITIAL_CODE, additional_heading: str = "") -> Dict[str, Any]:
    # Set code editor heading
    if additional_heading:
        editor_info_bar = deepcopy(EDITOR_INFO_BAR)
        editor_info_bar["info"][0]["name"] = f"Java - {additional_heading}"
    else:
        editor_info_bar = EDITOR_INFO_BAR

    return code_editor(
        initial_code,
        lang="java",
        buttons=EDITOR_BUTTONS,
        info=editor_info_bar
    )
