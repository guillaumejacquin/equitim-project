import { useState } from 'react';
import Container from "@material-ui/core/Container";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { FaPiedPiperAlt } from 'react-icons/fa';
import { FaInternetExplorer } from 'react-icons/fa';
import { ButtonGroup } from '@material-ui/core';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import { FaJs } from 'react-icons/fa';
import Page2 from "./page2";
import DatePicker from '@mui/lab/DatePicker';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';


const Page_beta = ({ formData, setForm, navigation }) => { 
  const { go } = navigation;

  const { firstName, lastName, nickName } = formData;

  const premiertab = () => {
    return(
      <div style={{width: "20%", border: '1px solid grey', borderRadius:"4%", height:"5%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}> <FaPiedPiperAlt/> Premier Bloc</h3>
          <TextField label="Nom" name="Nom" 
          style={{marginTop:"8%"}}
            onChange={(e)=>setNom(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <InputLabel style={{marginTop:"5%" }}id="F0">Typologie</InputLabel>
        <Select
          labelId="Typologie"
          id="Typologie"
          value={Typologie}
          label="Typologie"
          onChange={(e)=>setTypologie(e.target.value)}
          >
          <MenuItem value={"athéna"}>Athéna</MenuItem>
          <MenuItem value={"phoenix"}>Phoénix</MenuItem>


        </Select> 
        <InputLabel style={{marginTop:"5%" }}id="F0">Droit</InputLabel>
        <Select
          labelId="Droit"
          id="Droit"
          value={Droit_applicable}
          label="Droit"
          onChange={(e)=>setDroit(e.target.value)}
          >
          <MenuItem value={"français"}>français</MenuItem>
          <MenuItem value={"suisse"}>suisse</MenuItem>


        </Select> 

            <TextField
            label="ISIN"
            name="Isin"
            onChange={(e)=>setISIN(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

            <div style={{marginTop:"8%"}}></div>

            <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date d'émission"
                value={Emission}
                onChange={(Emission) => {
                  setEmission(Emission);
                }}
                renderInput={(params) => <TextField {...params} />}
              />


              </LocalizationProvider>
              <div style={{marginTop:"8%"}}></div>
              <TextField
            label="Dates de constatations initiales"
            name="DCI"
            onChange={(e)=>setDCI(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>


              <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date de premier remboursement"
                value={DR1}
                onChange={(DR1) => {
                  setDR1(DR1);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>


            
            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date de premier rappel"
                value={DPR}
                onChange={(DPR) => {
                  setDPR(DPR);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>


            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="avant derniere date de rappel"
                value={DADR}
                onChange={(DADR) => {
                  setDADR(DADR);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>


            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date de constatation finale"
                value={DCF}
                onChange={(DCF) => {
                  setDCF(DCF);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>

            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Date d'echeance"
                value={DEC}
                onChange={(DEC) => {
                  setDEC(DEC);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>

            <div style={{marginTop:"8%"}}></div>
              <LocalizationProvider dateAdapter={AdapterDateFns}>
              <DatePicker
                label="Avant derniere date de constatation finale"
                value={ADCF}
                onChange={(ADCF) => {
                  setADCF(ADCF);
                }}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>
      </Container>
    </div>
    )}

    const second_tab = () => {
      return(
        <div style={{width: "20%", height:"5%", border: '1px solid grey', borderRadius:"4%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}><FaInternetExplorer/> Second Bloc</h3>
  

      <InputLabel style={{marginTop:"5%" }}id="F0">Frequence</InputLabel>
        <Select
          labelId="F0"
          id="F0"
          value={F0}
          label="F0"
          onChange={(e)=>setF0(e.target.value)}
          >
          <MenuItem value={"jours"}>jours</MenuItem>
          <MenuItem value={"mois"}>mois</MenuItem>
          <MenuItem value={"trimestre"}>trimestre</MenuItem>
          <MenuItem value={"semestre"}>semestre</MenuItem>
          <MenuItem value={"année"}>année</MenuItem>

        </Select>
        <TextField
            label="TSJ"
            name="TSJ"
            onChange={(e)=>setTSJ(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
        <TextField
            label="sponsor1"
            name="PCS1"
            onChange={(e)=>setPCS1(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <TextField
            label="sponsor2"
            name="PCS2"
            onChange={(e)=>setPCS2(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
        
        <TextField
            label="sponsor3"
            name="PCS3"
            onChange={(e)=>setPCS3(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
        <TextField
            label="sponsor4"
            name="PCS4"
            onChange={(e)=>setPCS4(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <TextField
            label="sponsor5"
            name="PCS5"
            onChange={(e)=>setPCS5(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>


        <TextField
            label="CPN"
            name="CPN"
            onChange={(e)=>setCPN(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <TextField
            label="CPN_is_memoire"
            name="CPN_is_memoire"
            onChange={(e)=>setCPN_is_memoire(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
            
        <TextField
            label="PDI"
            name="PDI"
            onChange={(e)=>setPDI(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
      
      <TextField
            label="BAC"
            name="BAC"
            onChange={(e)=>setBAC(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

        <TextField
            label="BAC_is_degressif"
            name="BAC_is_degressif"
            onChange={(e)=>setBAC_is_degressif(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>

      <TextField
            label="BCPN"
            name="BCPN"
            onChange={(e)=>setBCPN(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
        <TextField
            label="BCPN_is_degressif"
            name="BCPN_is_degressif"
            onChange={(e)=>setBCPN_is_degressif(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth/>
        </Container>


        
      </div>
      )}

 
  const handleSubmit  = (event) => {
      event.preventDefault();

    // Simple POST request with a JSON body using fetch
    
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          Nom: Nom, Typologie:Typologie,
          Droit: Droit_applicable, Isin: Isin, Emission:Emission, DCI:DCI,
          DR1:DR1, DPR:DPR, DADR:DADR, DCF:DCF, DEC:DEC, ADCF:ADCF,
          F0:F0, TSJ:TSJ, PCS1:PCS1, PCS2:PCS2, PCS3:PCS3, PCS4:PCS4, PCS5:PCS5,
          CPN:CPN, CPN_is_memoire:CPN_is_memoire, PDI:PDI, 
          BAC:BAC, BAC_is_degressif:BAC_is_degressif, BCPN:BCPN, BCPN_is_degressif:BCPN_is_degressif,
          PEM:PEM, COM:COM, NSD:NSD, NSM:NSM, NSF:NSF,
          ABDAC:ABDAC, DBAC:DBAC, DEG:DEG, type_strike:type_strike,
          type_bar:type_bar, sous_jacent:sous_jacent, template:template
        })
    };
    
    fetch('http://localhost:5000/add', requestOptions)
        .then(response => response.json())
        .catch(error => console.log(error)) 
  }




  const [Nom, setNom] = useState('')
  const [Typologie, setTypologie] = useState('')
  const [Droit_applicable, setDroit] = useState('')
  const [Isin, setISIN] = useState('')
  const [Emission, setEmission] = useState('')
  const [DCI, setDCI] = useState('')
  const [DR1, setDR1] = useState('')
  const [DPR, setDPR] = useState('')
  const [DADR, setDADR] = useState('')
  const [DCF, setDCF] = useState('')
  const [DEC, setDEC] = useState('')
  const [ADCF, setADCF] = useState('')
  const [F0, setF0] = useState('')
  const [TSJ, setTSJ] = useState('')

  const [PCS1, setPCS1] = useState('')
  const [PCS2, setPCS2] = useState('')
  const [PCS3, setPCS3] = useState('')
  const [PCS4, setPCS4] = useState('')
  const [PCS5, setPCS5] = useState('')

  
  const [CPN, setCPN] = useState('')
  const [CPN_is_memoire, setCPN_is_memoire] = useState('')
  const [PDI, setPDI] = useState('')
  const [BAC, setBAC] = useState('')
  const [BAC_is_degressif, setBAC_is_degressif] = useState('')
  const [BCPN, setBCPN] = useState('')
  const [BCPN_is_degressif, setBCPN_is_degressif] = useState('')

  const [PEM, setPEM] = useState('')
  const [COM, setCOM] = useState('')
  const [NSD, setNSD] = useState('')
  const [NSM, setNSM] = useState('')
  const [NSF, setNSF] = useState('')
  const [ABDAC, setABDAC] = useState('')
  const [DBAC, setDBAC] = useState('')
  const [DEG, setDEG] = useState('')
  const [type_strike, settype_strike] = useState('')
  const [type_bar, settype_bar] = useState('')
  const [sous_jacent, setsous_jacent] = useState('')
  const [template, settemplate] = useState('')

  
  const props = { formData, navigation};


return (
  <div style={{height: "100%"}}>
    <div>
    <ButtonGroup variant="outlined" aria-label="outlined button group" size="large" style={{marginLeft:"20%"}}>
      <Button  style={{maxWidth: '100px', maxHeight: '100px', minWidth: '200PX', minHeight: '100px'}} > UN               </Button>
      <Button onClick={() => navigation.go("Page2")} style={{maxWidth: '100px', maxHeight: '100px', minWidth: '200PX', minHeight: '100px'}} > DEUX</Button>
      <Button style={{maxWidth: '100px', maxHeight: '100px', minWidth: '200PX', minHeight: '100px'}}> TROIS </Button>
    </ButtonGroup>

    </div>
    <div style={{display: "flex", marginTop:"10%"}}>
      {premiertab()}
      {second_tab()}

      <div style={{width: "20%", height:"5%", border: '1px solid grey', borderRadius:"4%", marginLeft:"10%"}}>
        <Container maxWidth="xs" style={{marginTop: "10%", marginBottom:"10%"}}>
          <h3 style={{textAlign:"center"}}> <FaJs/> Troisieme bloc</h3>

          <TextField label="PEM" name="PEM"
            style={{marginTop:"8%"}}

            onChange={(e)=>setPEM(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
          
          <TextField
            label="COM"
            name="COM"
            onChange={(e)=>setCOM(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="NSD"
            name="NSD"
            onChange={(e)=>setNSD(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
        <TextField
            label="NSM"
            name="NSM"
            onChange={(e)=>setNSM(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="NSF"
            name="NSF"
            onChange={(e)=>setNSF(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="ABDAC"
            name="ABDAC"
            onChange={(e)=>setABDAC(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

        <TextField
            label="DBAC"
            name="DBAC"
            onChange={(e)=>setDBAC(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />
        <TextField
            label="DEG"
            name="DEG"
            onChange={(e)=>setDEG(e.target.value)}
            margin="normal"
            variant="outlined"
            autoComplete="on"
            fullWidth
          />

    <InputLabel style={{marginTop:"5%" }}id="F0">type strike</InputLabel>
        <Select
          labelId="type_strike"
          id="type_strike"
          value={type_strike}
          label="type_strike"
          onChange={(e)=>settype_strike(e.target.value)}
          >
          <MenuItem value={"best strike"}>strike normal</MenuItem>
          <MenuItem value={"strike moyen"}>strike moyen</MenuItem>
          <MenuItem value={"best strike"}>best strike</MenuItem>

        </Select>


        <InputLabel style={{marginTop:"5%" }}id="F0">type bar</InputLabel>
        <Select
          labelId="type_bar"
          id="type_bar"
          value={type_bar}
          label="type_bar"
          onChange={(e)=>settype_bar(e.target.value)}
          >
          <MenuItem value={"degressif"}>dégressif</MenuItem>
          <MenuItem value={"airbag"}>airbag</MenuItem>
        </Select> 


        <InputLabel style={{marginTop:"5%" }}id="F0">sous jacent</InputLabel>
        <Select
          labelId="sous_jacent"
          id="sous_jacent"
          value={sous_jacent}
          label="sous_jacent"
          onChange={(e)=>setsous_jacent(e.target.value)}
          >
          <MenuItem value={"mono action"}>mono action</MenuItem>
          <MenuItem value={"wo action"}>wo action</MenuItem>
          <MenuItem value={"equipondéré action"}>équipondéré action</MenuItem>
          <MenuItem value={"mono indice"}>mono indice</MenuItem>
          <MenuItem value={"equipondéré indice"}>équipondéré indice</MenuItem>

        </Select> 

        <InputLabel style={{marginTop:"5%" }}id="F0">Template</InputLabel>
        <Select
          labelId="template"
          id="template"
          value={template}
          label="template"
          onChange={(e)=>settemplate(e.target.value)}
          >
          <MenuItem value={"testmercredi"}>testmercredi</MenuItem>

        </Select> 




        </Container>
      </div>
    </div>
          <Button
          variant="contained"
            
            color="primary"
            size="large"
            style={{ marginTop: "8%", left:"40%", width:"20%"}}
            onClick={handleSubmit}

          >
            Next
          </Button>

  </div>
);
  
}

export default Page_beta;


