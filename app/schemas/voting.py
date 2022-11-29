from pydantic import BaseModel, Field, validator


class VotingOptions(BaseModel):
    id: int
    name: str


class Voting(BaseModel):
    title: str
    options: list[VotingOptions]

    @validator("options", pre=True)
    def set_options_id(cls, v):  # задает id
        for i in range(len(v)):
            v[i]["id"] = i+1
        return v
