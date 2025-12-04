# tram

models for centraxx samples, patients, findings and else.

```
from tram import Sample, Identifier, Amount
sample = Sample(
  sampleid=Identifier(id="sample1", code="SAMPLEID"),
  type="EDTA",
  patientid=Idable(id="pat1", code="PSN"),
  restamount=Amount(value=1, unit="ml")
)
```

api doc [here](https://numlims.github.io/tram/).