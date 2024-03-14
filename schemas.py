from pydantic import BaseModel


class DataBase(BaseModel):
    Author_Full_Names: str
    Publication_Type: str
    Book_Editors: str
    Book_Group_Authors: str
    Author_Full_Names: str
    Book_Author_Full_Names: str
    Group_Authors: str
    Article_Title: str
    Source_Title: str
    Book_Series_Title: str
    Language: str
    Document_Type: str
    Conference_Title: str
    Conference_Date: str
    Conference_Location: str
    Conference_Sponsor: str
    Conference_Host: str
    Author_Keywords: str
    Keywords_Plus: str
    Abstract: str
    Addresses: str
    Affiliations: str
    Reprint_Addresses: str
    Email_Addresses: str
    Researcher_Ids: str
    ORCIDs: str
    Funding_Orgs: str
    Funding_Name_Preferred: str
    Funding_Text: str
    Cited_Reference_Count: str
    WoS_Core: str
    All_Databases: str
    Day_Usage_Count_180: str
    Since_2013_Usage_Count: str
    Publisher: str
    Publisher_City: str
    Publisher_Address: str
    ISSN: str
    eISSN: str
    ISBN: str
    Journal_Abbreviation: str
    Journal_ISO_Abbreviation: str
    Publication_Date: str
    Publication_Year: str
    Volume: str
    Issue: str
    Part_Number: str
    Supplement: str
    Special_Issue: str
    Meeting_Abstract: str
    Article_Number: str
    DOI: str
    Book_DOI: str
    Number_of_Pages: str
    WoS_Categories: str
    Web_of_Science_Index: str
    Research_Areas: str
    IDS_Number: str
    Pubmed_Id: str
    Open_Access_Designations: str
    UT: str


class Data(DataBase):
    Affiliations: str

    class Config:
        orm_mode = True


class DataYear(DataBase):
    Publication_Year: str


class DataUt(DataBase):
    UT: str


class DataName(DataBase):
    Author_Full_Names: str


class DataPub(DataBase):
    Publisher: str
