import { useState } from "react";
import { Box, TextField, Button, Typography } from "@mui/material";
import { colorPalletes } from "../App";

function DetectLanguage() {
  const [text, setText] = useState("");
  const changeText = (e) => {
    setText(e.target.value);
    console.log(text);
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
          id="outlined-basic"
          value={text}
          onChange={changeText}
          label="Teks"
          variant="outlined"
          //   size="small"
          sx={{ margin: "0 15px" }}
        />
        <Button
          variant="contained"
          sx={{
            margin: "0 15px",
            backgroundColor: colorPalletes.color3,
          }}
        >
          Detect
        </Button>
      </Box>
      <Typography sx={{ textAlign: "center", marginTop: "20px" }}>
        Bahasa Terdeteksi: {text}
      </Typography>
    </Box>
  );
}

export default DetectLanguage;
