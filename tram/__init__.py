
from datetime import datetime

class Identifier:
    def __init__(self, id=None, code:str=None):
        self.id = id
        self.code = code
class Amount:
    def __init__(self, value:float=None, unit:str=None):
        self.value = value
        self.unit = unit
    def __str__(self):
        out = str(self.value)
        if self.unit is not None:
            out += " " + self.unit
        return out
class Idable:
    def __init__(self, ids:list=None, mainidc:str=None, id=None, code:str=None):
        self.ids = ids
        if self.ids is None:
            self.ids = []
        self.mainidc = mainidc
        if id is not None:
            if ids is not None:
                raise Exception("Idable doesn't accept a list of ids if a single id is passed.")
            if mainidc is None:
                self.mainidc = code
            self.ids.append(Identifier(id=id, code=code))
    def identifier(self, code:str=None) -> Identifier:
        if code == None:
            code = self.mainidc
        for identifier in self.ids:
            if identifier.code == code:
                return identifier
    def id(self, code:str=None) -> str:
        if self.identifier(code) is not None:
            return self.identifier(code).id
        return None
    def set_id(self, code:str=None, id:str=None):
        for identifier in self.ids:
            if identifier.code == code:
                identifier.id = id
                return
        self.ids.append( Idable(id=id, code=code) )
    def iddict(self, *idcs):
        d = self.__dict__.copy()
        if idcs == None or len(idcs) == 0:
            idcs = [id.code for id in self.ids]
        for idc in idcs:
            d[idc] = self.id(idc)
        del d["ids"]
        del d["mainidc"]
        return d
    def __str__(self):
        if self.id() is not None:
            return self.id()
        return ""
class Sample(Idable):
    appointment:str = None
    category:str = None
    concentration=None
    creationdate:datetime=None
    derivaldate:datetime=None
    receiptdate:datetime=None
    first_repositiondate:datetime=None
    initialamount:Amount=None
    locationname:str=None
    locationpath:str=None
    orga:str = None
    parent:Idable=None 
    patient:Idable = None
    project:str = None
    receptacle:str=None
    restamount:Amount=None
    samplingdate:datetime=None
    secondprocessing:str=None
    secondprocessingdate:datetime=None
    stockprocessing:str=None
    stockprocessingdate:datetime=None
    repositiondate:datetime=None
    trial:str=None
    type:str=None
    xposition:int=None
    yposition:int=None
    def __init__(self,
         appointment:str=None,
         category:str=None,
         change_date:datetime=None,
         change_id:int=None,
         change_kind:str=None,
         change_user:str=None,
         concentration=None, # str?
         creationdate:datetime=None,
         cxxkitid:str=None,
         derivaldate:datetime=None,
         first_repositiondate:datetime=None,
         ids:Idable=None, 
         initialamount:Amount=None,
         kitid:str=None,
         locationpath:str=None,
         locationname:str=None,
         orga:str=None,
         parent:Idable=None,
         patient:Idable=None,
         project:str=None,
         receptacle:str=None, 
         restamount:Amount=None,
         samplingdate:datetime=None,
         secondprocessing:str=None,
         secondprocessingdate:datetime=None,         
         stockprocessing:str=None,
         stockprocessingdate:datetime=None,         
         receiptdate:datetime=None,         
         repositiondate:datetime=None,
         trial:str=None,
         type:str=None,
         xposition:int=None, 
         yposition:int=None
         ):
        Idable.__init__(self, ids.ids, ids.mainidc)
        self.appointment = appointment
        self.category = category
        self.change_date = change_date
        self.change_id = change_id
        self.change_kind = change_kind
        self.change_user = change_user
        self.concentration = concentration
        self.cxxkitid = cxxkitid        
        self.creationdate = creationdate
        self.derivaldate = derivaldate
        self.receiptdate = receiptdate
        self.first_repositiondate = first_repositiondate
        self.initialamount = initialamount
        self.kitid = kitid
        self.locationpath = locationpath
        self.locationname = locationname
        self.orga = orga
        self.parent = parent
        self.patient = patient
        self.project = project
        self.receptacle = receptacle
        self.repositiondate = repositiondate
        self.restamount = restamount
        self.secondprocessing = secondprocessing
        self.secondprocessingdate = secondprocessingdate        
        self.stockprocessing = stockprocessing
        self.stockprocessingdate = stockprocessingdate        
        self.samplingdate = samplingdate        
        self.trial = trial
        self.type = type
        self.xposition = xposition
        self.yposition = yposition
    def default(self, o):
        return o.__dict__
    @property
    def sampleid(self):
        return "bla" # self.get_id()
    def __getstate__(self):
        state = self.__dict__.copy() # is this slow?
        state["sampleid"] = self.id()
        state["patientid"] = self.patient.id() if self.patient else None
        return state
class Patient(Idable):
    def __init__(
      self,
      ids:Idable=None,
      orga:str=None
    ):
        #print("ids: " + str(ids.ids))
        Idable.__init__(self, ids.ids, ids.mainidc)
        self.orga = orga
    def __getstate__(self):
        state = self.__dict__.copy() # is this slow?
        state["patientid"] = self.id()
        return state
class Finding:
    method:str=None
    findingdate:datetime=None
    name:str=None
    patient:Idable=None
    recs:map={} # of Rec, by code
    sample:Idable
    sender:str=None
    def __init__(
        self,
        findingdate:datetime=None,
        method:str=None,
        name:str=None,
        patient:Idable=None,        
        recs:map={}, # of Rec, by code
        sample:Idable=None,
        sender:str=None,
    ):
        self.findingdate = findingdate
        self.method = method
        self.name = name
        self.patient = patient
        self.recs = recs
        self.sample = sample
        self.sender = sender
class User:
    def __init__(self,
      address:Address=None,
      divisional_admin:bool=None,
      firstname:str=None,      
      lastlogin:datetime=None,
      lastname:str=None,    
      username:str=None):
        self.address = address
        self.divisional_admin = divisional_admin
        self.firstname = firstname        
        self.lastlogin = lastlogin
        self.lastname = lastname        
        self.username = username
class Address:
    def __init__(self,
      country_descriptor:str=None,
      city:str=None,
      email:str=None,
      fax:str=None,
      mobile:str=None,
      phone1:str=None,
      phone2:str=None,
      street:str=None,
      street_no:str=None,
      zip_code:str=None,
      po_box:str=None,
      contact_person:str=None,
      contact:number=None
      ):
        self.country_descriptor = country_descriptor
        self.city = city
        self.email = email
        self.fax = fax
        self.mobile = mobile
        self.phone1 = phone1
        self.phone2 = phone2
        self.street = street
        self.street_no = street_no
        self.zip_code = zip_code
        self.po_box = po_box
        self.contact_person = contact_person
        self.contact = contact
class Trial:
    def __init__(self,
      code:str=None,
      name:str=None,
      orgas:list=None,
      users:list=None,
      ):
        self.code = code
        self.name = name
        self.orgas = orgas
        self.users = users
class Location:
    def __init__(self, schema:str=None, path:str=None):
        self.schema = schema
        self.path = path

class Rec:
    method:str = None
    labval:str = None
    type:str = None
    def __init__(self, method:str=None, labval:str=None):
        self.labval = labval
class BooleanRec(Rec):
    rec:bool = None
    def __init__(self, method:str=None, labval:str=None, rec:bool=None):
        Rec.__init__(self, method=method, labval=labval)
        self.rec = rec
class NumberRec(Rec):
    rec:float = None
    unit:str = None
    def __init__(self, method:str=None, labval:str=None, rec:float=None, unit:str=None):
        Rec.__init__(self, method=method, labval=labval)
        self.rec = rec
        self.unit = unit
class StringRec(Rec):
    rec:str = None
    def __init__(self, method:str=None, labval:str=None, rec:str=None):
        Rec.__init__(self, method=method, labval=labval)
        self.rec = rec
class DateRec(Rec):
    rec:datetime = None
    def __init__(self, method:str=None, labval:str=None, rec:datetime=None):
        Rec.__init__(self, method=method, labval=labval)
        self.rec = rec
class CatalogRec(Rec):
    rec:list = None
    rec_name:map = {}
    catalog:str = None
    def __init__(self, method:str=None, labval:str=None, rec:list=None, rec_name:map=None, catalog:str=None):
        Rec.__init__(self, method=method, labval=labval)
        self.rec = rec
        self.rec_name = rec_name
        self.catalog = catalog
class MultiRec(Rec):
    rec:list = None
    rec_name:map = {}
    def __init__(self, method:str=None, labval:str=None, rec:list=None, rec_name:map=None):
        Rec.__init__(self, method=method, labval=labval)
        if rec_name is None: # avoid mutable default params
            rec_name = {}
        self.rec = rec
        self.rec_name = rec_name

