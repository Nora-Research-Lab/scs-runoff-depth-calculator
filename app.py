import gradio as gr
from scs_runoff_depth_calculator import calculate_runoff

def run_calculation(cn, rainfall, amc):
    try:
        results = calculate_runoff(cn, rainfall, amc)
        
        return (
            str(results['adjusted_cn']),
            f"{results['s_in']:0.2f}",
            f"{results['ia_in']:0.2f}",
            f"{results['q_in']:0.2f}",
            f"{results['q_mm']:0.2f}",
            f"{results['runoff_ratio_percent']:0.2f}%"
        )
    except Exception as e:
        # Return empty strings or default values in case of error
        return ("", "", "", "", "", "")

with gr.Blocks(title="SCS Curve Number Runoff Calculator") as demo:
    gr.Markdown("# SCS Curve Number Runoff Calculator")
    
    with gr.Row():
        cn_input = gr.Slider(
            label="Curve Number (CN)",
            minimum=30,
            maximum=100,
            step=1,
            value=75
        )
        rainfall_input = gr.Number(
            label="Total Rainfall Depth (inches)",
            minimum=0,
            maximum=20,
            step=0.01,
            value=5.0
        )
    
    with gr.Row():
        amc_input = gr.Dropdown(
            label="Antecedent Moisture Condition (AMC)",
            choices=['AMC II (Average)', 'AMC I (Dry)', 'AMC III (Wet)'],
            value='AMC II (Average)'
        )
    
    with gr.Row():
        compute_btn = gr.Button("Compute Runoff", variant="primary")
    
    with gr.Row():
        with gr.Column():
            adjusted_cn_output = gr.Textbox(label="Adjusted Curve Number", interactive=False)
            s_output = gr.Textbox(label="Potential Maximum Retention S (in)", interactive=False)
            ia_output = gr.Textbox(label="Initial Abstraction Ia (in)", interactive=False)
        with gr.Column():
            q_in_output = gr.Textbox(label="Direct Runoff Q (in)", interactive=False)
            q_mm_output = gr.Textbox(label="Direct Runoff Q (mm)", interactive=False)
            runoff_ratio_output = gr.Textbox(label="Runoff Ratio (%)", interactive=False)
    
    compute_btn.click(
        fn=run_calculation,
        inputs=[cn_input, rainfall_input, amc_input],
        outputs=[
            adjusted_cn_output,
            s_output,
            ia_output,
            q_in_output,
            q_mm_output,
            runoff_ratio_output
        ]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
