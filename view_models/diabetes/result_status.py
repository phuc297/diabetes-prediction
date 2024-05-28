from typing import Optional
from starlette.requests import Request

from view_models.shared.view_model import ViewModelBase
from controllers import diabetes_predict

class ResultStatusViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.preg: Optional[str] = ''
        self.glu: Optional[str] = ''
        self.skin: Optional[str] = ''
        self.bmi: Optional[str] = ''
        self.age: Optional[str] = ''
        self.message: Optional[str] = None
    
    async def load(self):
        form = await self.request.form()
        self.preg = form.get('preg')
        self.glu = form.get('glu')
        self.skin = form.get('skin')
        self.bmi = form.get('bmi')
        self.age = form.get('age')

    def diabetes_predict(self):
        self.message = diabetes_predict.diabetes_predict(int(self.preg), int(self.glu), int(self.skin), int(self.bmi), int(self.age))
        
        

        