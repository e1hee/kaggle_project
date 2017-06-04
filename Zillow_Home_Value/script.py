# -*- coding: utf-8 -*-
"""
Created on Tue May 30 00:26:12 2017

@author: poioi
"""

import numpy as np
import pandas as pd

properties = pd.read_csv('data/properties_2016.csv')
transaction = pd.read_csv('data/train_2016.csv')
properties.rename(columns={'parcelid':'id_parcel', 'yearbuilt': 'build_year', 'basementsqft':'area_basement', 'yardbuildingsqft17':'area_patio',
                   'yardbuildingsqft26':'area_shed', 'poolsizesum':'area_pool', 'lotsizesquarefeet':'area_lot', 'garagetotalsqft':'area_garage',
                   'finishedfloor1squarefeet': 'area_firstfloor_finished', 'calculatedfinishedsquarefeet':'area_total_calc',
                   'finishedsquarefeet6':'area_base', 'finishedsquarefeet12':'area_live_finished','finishedsquarefeet13':'area_liveperi_finished',
                   'finishedsquarefeet15':'area_total_finished','finishedsquarefeet50':'area_unknown', 'unitcnt':'num_unit',
                   'numberofstories':'num_story', 'roomcnt':'num_room', 'bathroomcnt': 'num_bathroom', 'bedroomcnt':'num_bedroom',
                   'calculatedbathnbr':'num_bathroom_calc', 'fullbathcnt':'num_bath', 'threequarterbathnbr':'num_75_bath',
                   'fireplacecnt':'num_fireplace','poolcnt':'num_pool','garagecarcnt':'num_garage','regionidcounty':'region_county',
                   'regionidcity':'region_city', 'regionidzip':'region_zip', 'regionidneighborhood':'region_neighbor',
                   'taxvaluedollarcnt':'tax_total', 'structuretaxvaluedollarcnt':'tax_building', 'landtaxvaluedollarcnt':'tax_land',
                   'taxamount':'tax_property','assessmentyear':'tax_year','taxdelinquencyflag':'tax_delinquency',
                   'taxdelinquencyyear':'tax_delinquency_year','propertyzoningdesc':'zoning_property',
                   'propertylandusetypeid':'zoning_landuse', 'propertycountylandusecode':'zoning_landuse_county',
                   'fireplaceflag':'flag_fireplace','hashottuborspa':'flag_tub','buildingqualitytypeid':'quality',
                   'buildingclasstypeid':'framing', 'typeconstructiontypeid':'material','decktypeid':'deck',
                   'storytypeid':'story','heatingorsystemtypeid':'heating','airconditioningtypeid':'aircon',
                   'architecturalstyletypeid':'architectural_style'}, inplace=True)
    
transaction.rename(columns={'parcelid':'id_parcel','transactiondate':'date'})

list_y = ['tax_delinquency', 'flag_fireplace', 'flag_tub']
def change_y_1(df, lsts):
    for lst in lsts:
        df[lst] = df[lst].apply(lambda x: 1 if x == 'Y' else 0)
change_y_1(properties,list_y)