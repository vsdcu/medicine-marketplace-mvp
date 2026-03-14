import React from "react";

const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>Medicine Marketplace</h1>
      {children}
    </div>
  );
};

export default Layout;
