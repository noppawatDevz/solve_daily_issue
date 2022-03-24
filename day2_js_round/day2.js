const roundValue = (resp) => {
    for (let index = 0; index < resp.length; index++) {
        const element = resp[index];
        let roundVal = null;
        if (element._value != null && element._value != undefined) {
            const val = element._value;
            roundVal = Number(val.toFixed(4))
        }
        element._value = roundVal;
    }
}

const respOrder = [
    {
        "type": "1",
        "order_number": "001",
        "_value": 10.66067895959 
    },
    {
        "type": "1",
        "order_number": "002",
        "_value": 10.66067295959 
    },
    {
        "type": "1",
        "order_number": "003",
        "_value": 10.65  
    },
    {
        "type": "1",
        "order_number": "004",
        "_value": null 
    },
    {
        "type": "1",
        "order_number": "005",
        "_value": 7.222186565
    }
];

roundValue(respOrder);