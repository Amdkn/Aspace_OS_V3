import { ButtonHTMLAttributes, forwardRef } from "react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "emerald" | "outline" | "ghost";
  size?: "sm" | "md" | "lg";
}

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className = "", variant = "emerald", size = "md", children, ...props }, ref) => {
    const baseStyles =
      "inline-flex items-center justify-center gap-2 font-semibold uppercase tracking-[0.14em] rounded-sm transition-all disabled:shadow-none";

    const variants = {
      emerald:
        "bg-emerald-500 hover:bg-emerald-400 text-slate-950 emerald-glow-strong disabled:bg-slate-800 disabled:text-slate-600",
      outline:
        "border border-emerald-500/70 text-emerald-400 hover:bg-emerald-500/10 hover:text-white emerald-glow",
      ghost:
        "text-slate-400 hover:text-cream",
    };

    const sizes = {
      sm: "px-4 py-2 text-[12px]",
      md: "px-5 py-3 text-[13px]",
      lg: "px-6 py-4 text-[14px]",
    };

    return (
      <button
        ref={ref}
        className={`${baseStyles} ${variants[variant]} ${sizes[size]} ${className}`}
        {...props}
      >
        {children}
      </button>
    );
  }
);

Button.displayName = "Button";

export default Button;