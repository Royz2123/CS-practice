import json
import uuid
from copy import deepcopy
from typing import Any, Dict

from code_editor import code_editor
from streamlit.components.v1 import html

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
            "bottom": "2.50rem",
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
        "style": {"width": "1000px"}
    }]
}

DEFAULT_INITIAL_CODE = "print('hello world')\n\n\n"


def write_editor(
        initial_code: str = DEFAULT_INITIAL_CODE,
        additional_heading: str = "",
        read_only: bool = False
) -> Dict[str, Any]:
    # Create editable copies of the info bar and buttons
    editor_info_bar = deepcopy(EDITOR_INFO_BAR)
    editor_buttons = deepcopy(EDITOR_BUTTONS)

    # Set code editor heading
    if additional_heading:
        editor_info_bar["info"][0]["name"] = f"Java - {additional_heading}"

    # Set read only attributes
    if read_only:
        editor_info_bar["info"][0]["name"] += " (Read-Only)"
        editor_info_bar["css"] += "background-color: #e5bebe;"
        editor_buttons = [button for button in editor_buttons if button["name"] not in ["Run", "Test"]]

    # Return the code editor component
    editor_outputs = code_editor(
        initial_code,
        lang="java",
        buttons=editor_buttons,
        info=editor_info_bar
    )

    # Toggle readOnly property of the script
    html(
        f"""
            <script id={uuid.uuid4()}>
                console.log("Including readOnly script");
                function getIframe(iframeTitle) {{
                    console.log("Searching for iframe", iframeTitle);
                    let iframeElements = window.parent.document.getElementsByTagName("iframe")
                    for (let j = 0; j < iframeElements.length; j++){{
                        if (iframeElements[j].title == iframeTitle) {{
                            console.log("Found iframe titled", iframeTitle);
                            return iframeElements[j];
                        }}
                    }}
                    console.log("No iframe not found :(");
                    return null; 
                }}
                
                function setEditorReadOnly() {{
                    // First, make this iframe smaller on the way
                    let thisIframe = getIframe("st.iframe");
                    thisIframe.height = "1";
                    console.log("Set the readOnly iframe to minimal height")
                
                    // Now set the editor to readonly
                    let editorIframe = getIframe("code_editor.code_editor");
                    let textAreas = editorIframe.contentWindow.document.getElementsByClassName("ace_text-input");
                    for (let i = 0; i < textAreas.length; i++) {{
                        textAreas[i].readOnly = {json.dumps(read_only)};
                        console.log("Set element to readOnly =", {json.dumps(read_only)});
                    }} 
                }} 
                
                // Set trigger for iframe
                editorIframe = getIframe("code_editor.code_editor");
                editorIframe.addEventListener("load", setEditorReadOnly);
            </script>
        """,
    )

    return editor_outputs
