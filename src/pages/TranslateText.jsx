import { useState } from "react";
import {
  Box,
  TextField,
  Button,
  Typography,
  FormControl,
  Select,
  MenuItem,
} from "@mui/material";
import { colorPalletes } from "../App";

function TranslateText() {
  const [text, setText] = useState("");
  const [bahasaAsal, setBahasaAsal] = useState("id");
  const [bahasaTujuan, setBahasaTujuan] = useState("en");

  const changeText = (e) => {
    setText(e.target.value);
  };

  const changeBahasaAsal = (e) => {
    setBahasaAsal(e.target.value);
  };

  const changeBahasaTujuan = (e) => {
    setBahasaTujuan(e.target.value);
  };

  return (
    <Box>
      <Box
        sx={{
          display: "flex",
          marginTop: "15%",
          width: "100%",
          justifyContent: "center",
        }}
      >
        <TextField
          value={text}
          onChange={changeText}
          label="Teks"
          variant="outlined"
          size="normal"
          sx={{ margin: "0 15px" }}
        />
        <FormControl sx={{ minWidth: 200, margin: "0 15px" }}>
          {/* <InputLabel>Bahasa Asal</InputLabel> */}
          <Select
            displayEmpty
            inputProps={{ "aria-label": "Without label" }}
            value={bahasaAsal}
            onChange={changeBahasaAsal}
          >
            <MenuItem value="id">Indonesia</MenuItem>
            <MenuItem value="en">Inggris</MenuItem>
          </Select>
        </FormControl>
        <FormControl sx={{ minWidth: 200, margin: "0 15px" }}>
          {/* <InputLabel>Bahasa Tujuan</InputLabel> */}
          <Select
            displayEmpty
            inputProps={{ "aria-label": "Without label" }}
            value={bahasaTujuan}
            onChange={changeBahasaTujuan}
          >
            <MenuItem value="id">Indonesia</MenuItem>
            <MenuItem value="en">Inggris</MenuItem>
          </Select>
        </FormControl>
        <Button
          variant="contained"
          sx={{
            margin: "0 15px",
            backgroundColor: colorPalletes.color3,
            width: "120px",
          }}
        >
          Detect
        </Button>
      </Box>
      <Typography sx={{ textAlign: "center", marginTop: "20px" }}>
        Hasil Terjemahan: {text}
      </Typography>
    </Box>
  );
}

export default TranslateText;
