const config = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {},
  },

  plugins: [require("daisyui")],
  daisyui: {
    // TODO: Rewrite themes, these are bad
    themes: [
      {
        light: {
          primary: "#ef4444",
          "primary-content": "#FFFFFF",
          secondary: "#fb923c",
          accent: "#37CDBE",
          // TODO: Change this color
          neutral: "#3D4451", 
          "base-100": "#FFFFFF",
          info: "#3ABFF8",
          success: "#36D399",
          warning: "#FBBD23",
          error: "#F87272",
          // TODO: Change this color
          "error-content": "#FFFFFF"
        },
      },
      {
        dark: {
          primary: "#ef4444",
          secondary: "#fb923c",
          "primary-content": "FFFFFF",
          accent: "#37CDBE",
          neutral: "#3D4451",
          "base-100": "#1f2937",
          info: "#3ABFF8",
          success: "#36D399",
          warning: "#FBBD23",
          error: "#F87272",
        },
      },
    ],
  },
};

module.exports = config;
