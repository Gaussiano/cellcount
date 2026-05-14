use pyo3::prelude::*;

#[pyfunction]
fn fast_sum(values: Vec<f64>) -> f64 {
    values.iter().sum()
}

#[pymodule]
fn cellcount_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fast_sum, m)?)?;
    Ok(())
}