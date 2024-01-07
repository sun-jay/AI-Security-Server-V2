import Document, { Head, Html, Main, NextScript } from "next/document";

class MyDocument extends Document {
  render() {
    return (
      <Html lang="en">
        <Head>
        <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'></link>
          <link rel="icon" href="/favicon.ico" />
          <meta
            name="description"
            content="Search the SRVUSD course catalog"
          />

        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;
