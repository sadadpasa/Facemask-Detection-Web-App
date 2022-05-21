import * as React from "react";
import "./App.css";
import { Route, Routes, NavLink, useLocation } from "react-router-dom";
import {
  Box,
  Drawer,
  AppBar,
  Toolbar,
  Typography,
  List,
  ListItem,
  ListItemButton,
} from "@mui/material";

import Home from "./pages/Home";
import DetectLanguage from "./pages/DetectLanguage";
import SentenceLength from "./pages/SentenceLength";
import TranslateText from "./pages/TranslateText";
import TransLiterate from "./pages/TransLiterate";

const routes = [
  {
    path: "/",
    main: () => <Home />,
  },
  {
    path: "/detect-language",
    main: () => <DetectLanguage />,
  },
  {
    path: "/translate-text",
    main: () => <TranslateText />,
  },
  {
    path: "/trans-literate",
    main: () => <TransLiterate />,
  },
  {
    path: "/sentence-length",
    main: () => <SentenceLength />,
  },
];

const drawerWidth = 240;
export const colorPalletes = {
  color1: "#234979",
  color2: "#346DB6",
  color3: "#4691F2",
  color4: "#A2C8F9",
  color5: "#D1E3FC",
  color6: "#5E646A",
  color7: "#FFFFFF",
};
export const ColorPalletesContext = React.createContext(colorPalletes);

export default function App() {
  const location = useLocation();
  const { pathname } = location;
  const splitLocation = pathname.split("/");
  return (
    <Box sx={{ display: "flex" }}>
      <AppBar
        position="fixed"
        sx={{
          zIndex: (theme) => theme.zIndex.drawer + 1,
          backgroundColor: colorPalletes.color7,
        }}
      >
        <Toolbar>
          <Typography
            sx={{ color: colorPalletes.color3 }}
            variant="h6"
            noWrap
            component="div"
          >
            Aplikasi Web Translator
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          [`& .MuiDrawer-paper`]: {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
      >
        <Toolbar />
        <List sx={{ py: "0" }}>
          <NavLink exact to="/">
            <ListItem
              key="home"
              disablePadding
              className={splitLocation[1] === "" ? "sidebar-active" : ""}
            >
              <ListItemButton>
                <Typography
                  className={splitLocation[1] === "" ? "sidebar-active" : ""}
                  color={colorPalletes.color6}
                  sx={{ fontWeight: "bold" }}
                >
                  Home
                </Typography>
              </ListItemButton>
            </ListItem>
          </NavLink>
          <NavLink to="/detect-language">
            <ListItem
              key="detect-language"
              disablePadding
              className={
                splitLocation[1] === "detect-language" ? "sidebar-active" : ""
              }
            >
              <ListItemButton>
                <Typography
                  className={
                    splitLocation[1] === "detect-language"
                      ? "sidebar-active"
                      : ""
                  }
                  color={colorPalletes.color6}
                  sx={{ fontWeight: "bold" }}
                >
                  Detect Language
                </Typography>
              </ListItemButton>
            </ListItem>
          </NavLink>
          <NavLink to="/translate-text">
            <ListItem
              key="translate-text"
              disablePadding
              className={
                splitLocation[1] === "translate-text" ? "sidebar-active" : ""
              }
            >
              <ListItemButton>
                <Typography
                  className={
                    splitLocation[1] === "translate-text"
                      ? "sidebar-active"
                      : ""
                  }
                  color={colorPalletes.color6}
                  sx={{ fontWeight: "bold" }}
                >
                  Translate Text
                </Typography>
              </ListItemButton>
            </ListItem>
          </NavLink>
          <NavLink to="/trans-literate">
            <ListItem
              key="trans-literate"
              disablePadding
              className={
                splitLocation[1] === "trans-literate" ? "sidebar-active" : ""
              }
            >
              <ListItemButton>
                <Typography
                  className={
                    splitLocation[1] === "trans-literate"
                      ? "sidebar-active"
                      : ""
                  }
                  color={colorPalletes.color6}
                  sx={{ fontWeight: "bold" }}
                >
                  Trans Literate
                </Typography>
              </ListItemButton>
            </ListItem>
          </NavLink>
          <NavLink to="/sentence-length">
            <ListItem
              key="sentence-length"
              disablePadding
              className={
                splitLocation[1] === "sentence-length" ? "sidebar-active" : ""
              }
            >
              <ListItemButton>
                <Typography
                  className={
                    splitLocation[1] === "sentence-length"
                      ? "sidebar-active"
                      : ""
                  }
                  color={colorPalletes.color6}
                  sx={{ fontWeight: "bold" }}
                >
                  Get Sentence Length
                </Typography>
              </ListItemButton>
            </ListItem>
          </NavLink>
        </List>
      </Drawer>
      <Box component="main" sx={{ flexGrow: 1 }}>
        <Toolbar />
        <Routes>
          {routes.map(({ path, main }) => (
            <Route key={path} path={path} element={main()} />
          ))}
        </Routes>
      </Box>
    </Box>
  );
}
