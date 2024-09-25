/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      spacing: {
        md: '1.5rem',
        card: '3rem',
        icon: '1.25rem',
      },
      gridTemplateColumns: {
        endDateLayout: 'calc(50% - 0.5rem) 1fr auto',
      },
      aspectRatio: {
        a4: '1/1.414'
      },
      fontFamily: {
        custom: ['Roboto', 'sans-serif'],
      },
      fontSize: {
        tpHead: 'var(--tp-head)',
        tpTitle: 'var(--tp-title)',
        tpSubtitle: 'var(--tp-subtitle)',
        tpBody: 'var(--tp-body)',
      },
      colors: {
        tpPrimary: "var(--tp-primary)",
        tpSecondary: "var(--tp-secondary)",
        tpThird: "var(--tp-third)",
        tpDark: "var(--tp-dark)",
        tpLight: "var(--tp-light)",
      }
    },
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: [
      {
        light: {
          ...require("daisyui/src/theming/themes")["light"],
          'primary': '#f39200',
          'primary-content': '#f4f4f4',
          'base-100': '#f1f1f1',
          'base-200': '#fafafa',
          'base-300': '#c7c7c7',
          'base-content': '#1d232a',
          'info': '#0167d8',
          'success': '#37b358',
          'success-content': '#f4f4f4',
          'warning': '#ef9400',
          'error': '#eb4236',
          'error-content': '#f4f4f4',
        },
      },
      {
        dark: {
          ...require("daisyui/src/theming/themes")["dark"],
          'primary': '#f39200',
          'primary-content': '#f4f4f4',
          'base-300': '#2e353d',
          'base-content': '#f4f4f4',
          'info': '#0167d8',
          'success': '#37b358',
          'success-content': '#f4f4f4',
          'warning': '#ef9400',
          'error': '#eb4236',
          'error-content': '#f4f4f4',
        },
      },
    ],
    darkTheme: "dark",
    base: false,
  }
}