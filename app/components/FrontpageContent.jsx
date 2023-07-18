import React from 'react'

const text = {
    boxSizing: "border-box",
    flexShrink: 0,
    width: "100%",
    height: "min-content", /* 547px */
    display: "flex",
    flexDirection: "column",
    justifyContent: "flex-start",
    alignItems: "center",
    padding: "100px 100px 100px 100px",
    backgroundColor: "#ffffff",
    overflow: "visible",
    position: "relative",
    alignContent: "center",
    flexWrap: "nowrap",
    gap: 0,
    borderRadius: "0px 0px 0px 0px",
  }

  const content = {
    flexShrink: 0,
    width: "100%",
    height: "min-content", /* 347px */
    display: "flex",
    flexDirection: "column",
    justifyContent: "flex-start",
    alignItems: "flex-start",
    maxWidth: 1000,
    overflow: "visible",
    zIndex: 1,
    position: "relative",
    padding: "0px 0px 0px 0px",
    alignContent: "flex-start",
    flexWrap: "nowrap",
    gap: 40,
    borderRadius: "0px 0px 0px 0px",
  }

  const enchanting = {
    flexShrink: 0,
    width: "100%",
    height: "auto", /* 58px */
    whiteSpace: "pre-wrap",
    wordWrap: "break-word",
    wordBreak: "break-word",
    overflow: "visible",
    position: "relative",
    fontWeight: 400,
    fontStyle: "normal",
    fontFamily: `"Limelight", sans-serif`,
    color: "#1d3557",
    fontSize: 48,
    letterSpacing: "0em",
    lineHeight: 1.2,
    textAlign: "left",
  }

  const embark = {
    flexShrink: 0,
    width: "100%",
    height: "auto", /* 249px */
    whiteSpace: "pre-wrap",
    wordWrap: "break-word",
    wordBreak: "break-word",
    overflow: "visible",
    position: "relative",
    fontWeight: 700,
    fontStyle: "normal",
    fontFamily: `"Inter", "Inter Placeholder", sans-serif`,
    color: "#000000",
    fontSize: 32,
    letterSpacing: "-0.05em",
    lineHeight: 1.3,
    textAlign: "left",
  }

const FrontpageContent = () => {
  return (
    <div className={`${text}`}>
      <div className={`${content}`}>
        <div className={`${enchanting}`}>
            Enchanting Items Await
        </div>
        <div className={`${embark}`}>
           Embark on a mystical journey to unveil extraordinary magical items hidden within the Dark Age of Camelot. It’s not just a fantasy MMO RPG game anymore, it’s your chance to harness the unparalleled power!
        </div>
      </div>
    </div>
  )
}

export default FrontpageContent
