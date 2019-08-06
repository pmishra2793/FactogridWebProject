from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from factogridApp.models import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# Create your views here.


def index(request):
    # return HttpResponse("I am back django")
    return render(request, 'index.html')


def addequipment(request):
    # get all the data from the equipment form
    if request.method == 'POST':
        Id = request.POST.get('equipId')
        Description = request.POST.get('equipDec')
        ActiveStatus = request.POST.get('equipAs')
        if ActiveStatus == 'on':
            ActiveStatus = True
        else:
            ActiveStatus = False

        # Update the table data based on the Id
        vId = Equipment.objects.filter(Id=Id).first() # if we write first() then we get only value instead off queryset
        if vId:
            vId.Description = Description
            vId.ActiveStatus = ActiveStatus
            vId.save()
        else:
            # If new Id comes then direct save into the database
            equfipment = Equipment(Id=Id,Description=Description,ActiveStatus=ActiveStatus)
            equfipment.save()

    vCommonfun = commonFun()
    return render(request, 'index.html', vCommonfun)

def addequipmentprop(request):
    # get all the equipment prop data
    if request.method == 'POST':
        vForeignId = request.POST.get('foreignId')
        vEquipPropId = request.POST.get('equipPropId')
        vEquipPropDesc = request.POST.get('equipPropDesc')
        vEquipPropValue = request.POST.get('equipPropValue')
        vUOM = request.POST.get('value')
        vEquipPropAs = request.POST.get('equipPropAs')
        if vEquipPropAs == 'on':
            vEquipPropAs = True
        else:
            vEquipPropAs = False


        # update the equipment prop table based on the Id
        vEquipPropData = EquipmentProp.objects.filter(propId=vEquipPropId).first()
        if vEquipPropData:
            vEquipPropData.propDesc = vEquipPropDesc
            vEquipPropData.propValue = vEquipPropValue
            vEquipPropData.propUOM = vUOM
            vEquipPropData.propAS = vEquipPropAs
            vEquipPropData.save()
        else:
            # checked the foreignId is available or not in the equipment table
            vEquipId = Equipment.objects.filter(Id=vForeignId).first()
            if vEquipId:
                equipmentProp = EquipmentProp(equipId=vEquipId,propId=vEquipPropId,propDesc=vEquipPropDesc,propValue=vEquipPropValue,propUOM=vUOM,propAS=vEquipPropAs)
                equipmentProp.save()
            else:
                pass

    vCommonfun = commonFun()
    return render(request, 'index.html', vCommonfun)

def commonFun():
    mainData = []
    # fetch all records from the database and display in the table
    vAllEquipment = Equipment.objects.all()
    equipArray = []
    for i in vAllEquipment:
        equipDict = {'AutoId': i.AutoId, 'Id': i.Id, 'Description': i.Description, 'ActiveStatus': i.ActiveStatus}
        equipArray.append(equipDict)
    paramsEquip = {'Equipments': equipArray}

    # fetch all the equipmnet prop item into the table
    vAllEquipmentProp = EquipmentProp.objects.all()
    equipmentProp = []
    for i in vAllEquipmentProp:
        equipPropDict = {'AutoId': i.id, 'foreginId': i.equipId.Id, 'Id': i.propId, 'Description': i.propDesc,
                         'Value': i.propValue, 'UOM': i.propUOM, 'ActiveStatus': i.propAS}
        equipmentProp.append(equipPropDict)
    paramsEquipProp = {'EquipmentProp': equipmentProp}

    mainData.append(paramsEquip)
    # mainData.append(paramsEquipProp)
    params = {'mainData': mainData}
    return params

@csrf_exempt
def equipPropData(request):
    import json
    vEquip = request.POST.get('equip')
    vEquipData = Equipment.objects.filter(Id=vEquip).first()
    if vEquipData:
        vPropEquipData = EquipmentProp.objects.filter(equipId=vEquipData)
        equipPropList = []
        for i in vPropEquipData:
            equipPropDict = {'AutoId': i.id, 'foreginId': i.equipId.Id, 'Id': i.propId, 'Description': i.propDesc,
                         'Value': i.propValue, 'UOM': i.propUOM, 'ActiveStatus': i.propAS}
            equipPropList.append(equipPropDict)
        params = {'EquipPropData':equipPropList}
        print ('params ==== ',params)
        # return HttpResponse(params)
        return HttpResponse(json.dumps(equipPropList), content_type='application/json')