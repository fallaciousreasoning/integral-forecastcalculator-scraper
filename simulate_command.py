def make_date_condition(month: str, year: int):
    return f'Date+=+[{month}+{year}]'


def make_age_condition(age: int):
    return f'Crop.Age+=+5'


def make_dos_condition(mm: float):
    return f'Crop.MeanLiftDOS+>+{mm}'


class SimulateCommand:
    def __init__(self, condition: str, event: dict) -> None:
        self.condition = condition
        self.event = event


DOMESTIC_PRAD_3P_T2_COMMANDS = [
    {
        "condition": "Date+=+[Jun+2000]",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PlantEventViewModel,+Scion.ForecasterCalculator",
            "species": "P.RAD",
            "plantStocking": 1000
        }
    },
    {
        "condition": "Crop.Age+=+5",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PruneEventViewModel,+Scion.ForecasterCalculator",
            "prunedStocking": 450,
            "prunedHeight": 2.4
        }
    },
    {
        "condition": "",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ThinEventViewModel,+Scion.ForecasterCalculator",
            "residualStocking": 700
        }
    },
    {
        "condition": "Crop.Age+=+7",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PruneEventViewModel,+Scion.ForecasterCalculator",
            "prunedStocking": 400,
            "prunedHeight": 4.6
        }
    },
    {
        "condition": "Crop.Age+=+10",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PruneEventViewModel,+Scion.ForecasterCalculator",
            "prunedStocking": 350,
            "prunedHeight": 6
        }
    },
    {
        "condition": "",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ThinEventViewModel,+Scion.ForecasterCalculator",
            "residualStocking": 350
        }
    },
    {
        "condition": "Crop.Age+=+30",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ClearfellEventViewModel,+Scion.ForecasterCalculator",
            "pricedLogProductDefinitions": [
                {
                    "name": "P",
                            "description": "Pruned+log",
                            "pricePerM3": 126,
                            "maxCut": 99,
                            "priority": 4
                },
                {
                    "name": "S1",
                            "description": "Large+sawlog+with+small+branches",
                            "pricePerM3": 88,
                            "maxCut": 99,
                            "priority": 6
                },
                {
                    "name": "S2",
                            "description": "Medium+sawlog+with+small+branches",
                            "pricePerM3": 80,
                            "maxCut": 99,
                            "priority": 7
                },
                {
                    "name": "S3",
                            "description": "Small+sawlog+with+small+branches",
                            "pricePerM3": 64,
                            "maxCut": 99,
                            "priority": 8
                },
                {
                    "name": "L1",
                            "description": "Large+sawlog+with+large+branches",
                            "pricePerM3": 65,
                            "maxCut": 99,
                            "priority": 1
                },
                {
                    "name": "L2",
                            "description": "Medium+sawlog+with+large+branches",
                            "pricePerM3": 56,
                            "maxCut": 99,
                            "priority": 2
                },
                {
                    "name": "L3",
                            "description": "Small+sawlog+with+large+branches",
                            "pricePerM3": 52,
                            "maxCut": 99,
                            "priority": 3
                },
                {
                    "name": "Pulp",
                            "description": "Pulp+log",
                            "pricePerM3": 40,
                            "maxCut": 99,
                            "priority": 5
                }
            ],
            "cuttingStrategyName": "Domestic+Radiata",
            "cuttingStrategyDescription": "Default+domestic+strategy",
            "specie": "P.RAD",
            "cutCost": 1,
            "buckingMode": "MaximumValue"
        }
    }
]

EXPORT_PRAD_3P_T2_COMMANDS = [
    {
        "condition": "Date+=+[Jun+2000]",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PlantEventViewModel,+Scion.ForecasterCalculator",
            "species": "P.RAD",
            "plantStocking": 1000
        }
    },
    {
        "condition": "Crop.Age+=+5",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PruneEventViewModel,+Scion.ForecasterCalculator",
            "prunedStocking": 450,
            "prunedHeight": 2.4
        }
    },
    {
        "condition": "",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ThinEventViewModel,+Scion.ForecasterCalculator",
            "residualStocking": 700
        }
    },
    {
        "condition": "Crop.Age+=+7",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PruneEventViewModel,+Scion.ForecasterCalculator",
            "prunedStocking": 400,
            "prunedHeight": 4.6
        }
    },
    {
        "condition": "Crop.Age+=+10",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PruneEventViewModel,+Scion.ForecasterCalculator",
            "prunedStocking": 350,
            "prunedHeight": 6
        }
    },
    {
        "condition": "",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ThinEventViewModel,+Scion.ForecasterCalculator",
            "residualStocking": 350
        }
    },
    {
        "condition": "Crop.Age+=+30",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ClearfellEventViewModel,+Scion.ForecasterCalculator",
            "pricedLogProductDefinitions": [
                {
                    "name": "Pruned",
                            "description": "Pruned",
                            "pricePerM3": 160,
                            "maxCut": 99,
                            "priority": 1
                },
                {
                    "name": "AO",
                            "description": "Large+Structural",
                            "pricePerM3": 113,
                            "maxCut": 99,
                            "priority": 2
                },
                {
                    "name": "A",
                            "description": "Structural",
                            "pricePerM3": 111,
                            "maxCut": 99,
                            "priority": 3
                },
                {
                    "name": "K",
                            "description": "Small+sawlog",
                            "pricePerM3": 100,
                            "maxCut": 99,
                            "priority": 4
                },
                {
                    "name": "KI",
                            "description": "Industrial+sawlog",
                            "pricePerM3": 92,
                            "maxCut": 99,
                            "priority": 5
                },
                {
                    "name": "KIS",
                            "description": "Small+Industrial+sawlog",
                            "pricePerM3": 85,
                            "maxCut": 99,
                            "priority": 6
                }
            ],
            "cuttingStrategyName": "Export+Radiata",
            "cuttingStrategyDescription": "Default+export+strategy",
            "specie": "P.RAD",
            "cutCost": 1,
            "buckingMode": "MaximumValue"
        }
    }
]

PSEM_1T_COMMANDS = [
    {
        "condition": "Date+=+[Jun+2000]",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.PlantEventViewModel,+Scion.ForecasterCalculator",
            "species": "PSMEN",
            "plantStocking": 1650
        }
    },
    {
        "condition": "Date+=+[Jun+2010]",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.MeasurementEventViewModel,+Scion.ForecasterCalculator",
            "stocking": 1500,
            "basalArea": 6.8,
            "meanTopHeight": 5.9
        }
    },
    {
        "condition": "Crop.Age+=+15",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ThinEventViewModel,+Scion.ForecasterCalculator",
            "residualStocking": 750
        }
    },
    {
        "condition": "Crop.Age+=+40",
        "event": {
            "$type": "Scion.ForecasterCalculator.Models.ClearfellEventViewModel,+Scion.ForecasterCalculator",
            "pricedLogProductDefinitions": [
                {
                    "name": "DS",
                            "description": "Sawlog",
                            "pricePerM3": 160,
                            "maxCut": 99,
                            "priority": 1
                },
                {
                    "name": "CF+",
                            "description": "",
                            "pricePerM3": 110,
                            "maxCut": 99,
                            "priority": 2
                },
                {
                    "name": "CF-",
                            "description": "",
                            "pricePerM3": 90,
                            "maxCut": 99,
                            "priority": 3
                },
                {
                    "name": "Pulp",
                            "description": "Pulp+log",
                            "pricePerM3": 40,
                            "maxCut": 99,
                            "priority": 4
                }
            ],
            "cuttingStrategyName": "Douglas-fir",
            "cuttingStrategyDescription": "",
            "specie": "PSMEN",
            "cutCost": 1,
            "buckingMode": "MaximumValue"
        }
    }
]
