# tram

models for centraxx samples, patients, findings and else.

```
from tram import Sample, Identifier
sample = Sample(
  sampleid=Identifier(id="sample1", code="SAMPLEID")
)
```

api doc [here](https://numlims.github.io/tram/).

## install

download tram whl from
[here](https://github.com/numlims/tram/releases). install whl with
pip:

```
pip install tram-<version>.whl
```

## use

make a sample that belongs to a patient and give it an amount.

```
sample = Sample(
  sampleid=Identifier(id="sample1", code="SAMPLEID"),
  type="EDTA",
  patientid=Idable(id="pat1", code="PSN", mainidc="PSN"),
  restamount=Amount(value=1, unit="ml")
)
```

Idables holds a collection of Identifiers, the code of the main id is
specified by mainidc.

make a finding and pass it a recorded value.

```
rec = StringRec(method="PATHO", labval="PATHOGEN", value="E-Coli")

finding = Finding(
    method="PATHOGEN",
    patient=Idable(id="pat1", code="PSN", mainidc="PSN"),
    recs=[rec],
    sample=Idable(id="samp1", code="SAMPLEID", mainidc="SAMPLEID"),
)
```