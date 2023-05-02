from data.model.complain import Complain
from data.repository.complain_repository_impl import ComplainRepositoryImpl
from dtos.request.complain_request import ComplainRequest
from dtos.response.complain_response import ComplainResponse
from services.complain_service import ComplainService
from utils.invalid_id import InvalidId
from utils.mapper import Mapper


class ComplainServiceImpl(ComplainService):
    complain_repository = ComplainRepositoryImpl()

    def log_complain(self, complain_request: ComplainRequest) -> ComplainResponse:
        complain = Mapper.map_complain_request_with_complain(complain_request)
        saved_complain = self.complain_repository.add(complain)
        complain_response = Mapper.map_complain_with_complain_response(saved_complain)
        return complain_response

    def check_complain_status(self, identity_number: int) -> str:
        complain = self.complain_repository.find_complain_by_id(identity_number)

        if not complain:
            raise InvalidId("Invalid Identity Number....")

        return self.status_completed_message()

    @staticmethod
    def status_completed_message():
        return "Complaint resolved"
