import React from "react";
import { Link } from "react-router-dom";

const OtherPage = () => {
  return (
    <div>
      This is a website for calculating Fibonacci numbers!
      <Link to="/">Go back home</Link>
    </div>
  );
};

export default OtherPage;
