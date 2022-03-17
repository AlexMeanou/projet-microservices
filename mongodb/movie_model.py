# from pydantic import BaseModel
# from bson import ObjectId

# class Movie(BaseModel):
#     _id: ObjectId
#     name: str
#     email: str
#     username: str

# class MovieModel(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     name: str = Field(...)
#     course: str = Field(...)
#     gpa: float = Field(..., le=4.0)
#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}
#         schema_extra = {
#             "example": {
#                 "name": "Jane Doe",
#                 "email": "jdoe@example.com",
#                 "course": "Experiments, Science, and Fashion in Nanophotonics",
#                 "gpa": "3.0",
#             }
        # }