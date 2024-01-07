import { Analytics } from "@vercel/analytics/react";
import type { AppProps } from "next/app";
import "../styles/globals.scss";
import userServices from "../firebase/userServices";
import { db, auth } from "../firebase/clientApp.js";
import { useState, useEffect } from "react";
import firebase from "firebase/compat/app";
import "firebase/compat/auth";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Component
        {...pageProps}
      />
      <Analytics />
    </>
  );
}

export default MyApp;
