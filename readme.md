# tram

models for centraxx samples, patients, findings and else.

```
from tram import Sample, Idable
sample = Sample(
  ids=Idable(id="sample1", code="SAMPLEID")
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
  ids=Idable(id="sample1", code="SAMPLEID"),
  type="EDTA",
  patientid=Idable(id="pat1", code="PSN", mainidc="PSN"),
  restamount=Amount(value=1, unit="ml")
)
```

Idable holds a collection of Identifiers, in this case, one with code SAMPLEID.

make a recorded value of type string.

```
rec = StringRec(method="PATHO", labval="PATHOGEN", value="E-Coli")
```

make a finding and pass it the recorded value.

```
finding = Finding(
    method="PATHOGEN",
    patient=Idable(ids=pids, mainidc="PSN"),
    recs=[rec],
    sample=Idable(ids=sids, mainidc="SAMPLEID"),
)
```

when a list of identifiers is passed to Idable, the code of the main
identifier (mainidc) can be given.