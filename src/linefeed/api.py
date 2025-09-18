from fastapi import FastAPI, Request, Depends, HTTPException
from pydantic import BaseModel
from .print_command import PrintCommand
from .formatter import Formatter
from .print_handler import PrintHandler


class PrintResponse(BaseModel):
    request_id: str


api = FastAPI()


def get_formatter(request: Request) -> Formatter:
    return request.app.state.formatter


def get_print_handler(request: Request) -> PrintHandler:
    return request.app.state.print_handler


@api.put("/print")
def new_print_command(
    command: PrintCommand,
    formatter: Formatter = Depends(get_formatter),
    print_handler: PrintHandler = Depends(get_print_handler),
) -> PrintResponse:
    try:
        formatted_segment = formatter.format(command)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
    try:
        request_id = print_handler.print(formatted_segment)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal failure during printing: {str(e)}"
        ) from e

    return PrintResponse(request_id=request_id)


@api.get("/status/{request_id}")
def get_print_status(
    request_id: str,
    print_handler: PrintHandler = Depends(get_print_handler),
) -> dict[str, str]:
    try:
        status = print_handler.get_status(request_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
    return {"status": status.name}
