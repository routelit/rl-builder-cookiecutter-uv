from flask import Flask, Response
from routelit import RouteLit  # type: ignore[import-untyped]
from routelit_flask import RouteLitFlaskAdapter  # type: ignore[import-untyped]

from {{cookiecutter.project_slug}} import RLBuilder  # type: ignore[import-untyped]

app = Flask(__name__)

routelit = RouteLit(BuilderClass=RLBuilder)
routelit_adapter = RouteLitFlaskAdapter(
    routelit,
    ### TO USE LOCAL VITE DEV SERVER, UNCOMMENT THE FOLLOWING LINES
    # run_mode="dev_components",
    # local_components_server="http://localhost:5173"
).configure(app)


def view(ui: RLBuilder) -> None:  # type: ignore[no-any-unimported]
    ui.hello("RouteLit")
    ui.hello_world()


@app.route("/", methods=["GET", "POST"])
def index() -> Response:
    return routelit_adapter.stream_response(view)  # type: ignore[no-any-return]


if __name__ == "__main__":
    app.run(debug=True)  # noqa: S201
