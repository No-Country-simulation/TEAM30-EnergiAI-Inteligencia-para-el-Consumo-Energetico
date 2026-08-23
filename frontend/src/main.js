import './style.css'

const API_URL = 'http://localhost:8080'

document.querySelector('#app').innerHTML = `
  <main class="min-h-screen bg-slate-950 text-white">

    <header class="border-b border-slate-800">
      <div class="mx-auto max-w-6xl px-6 py-5">
        <div class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between">

          <div>
            <img
              src="/energiai-logo.png"
              alt="EnergiAI"
              class="h-12 w-auto object-contain"
            />
          </div>

          <nav class="flex gap-2">

            <button
              id="nav-nuevo"
              type="button"
              class="rounded-lg bg-teal-400 px-4 py-2 text-sm font-semibold text-slate-950"
            >
              Nuevo análisis
            </button>

            <button
              id="nav-consultas"
              type="button"
              class="rounded-lg px-4 py-2 text-sm font-semibold text-slate-300 transition hover:bg-slate-800"
            >
              Consultas
            </button>

          </nav>

        </div>
      </div>
    </header>

    <section
      id="seccion-nuevo"
      class="mx-auto max-w-6xl px-6 py-12"
    >

      <div class="mb-10">

        <p class="mb-2 text-sm font-semibold uppercase tracking-wider text-teal-400">
          Nuevo análisis
        </p>

        <h2 class="text-4xl font-bold">
          Analizá tu consumo energético
        </h2>

        <p class="mt-3 max-w-2xl text-slate-400">
          Completá los datos de consumo para obtener un análisis energético.
        </p>

      </div>

      <div class="rounded-2xl border border-slate-800 bg-slate-900 p-6 md:p-8">

        <h3 class="mb-6 text-xl font-semibold">
          Datos del consumo
        </h3>

        <form
          id="analisis-form"
          class="grid gap-6 md:grid-cols-2"
        >

          <div>

            <label
              for="usuario-id"
              class="mb-2 block text-sm text-slate-300"
            >
              Número de Cliente
            </label>

            <input
              id="usuario-id"
              type="number"
              min="1"
              placeholder="Ej: 4"
              class="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-teal-400"
              required
            />

          </div>

          <div>

            <label
              for="consumo-kwh"
              class="mb-2 block text-sm text-slate-300"
            >
              Consumo mensual (kWh)
            </label>

            <input
              id="consumo-kwh"
              type="number"
              min="0"
              step="0.01"
              placeholder="Ej: 420"
              class="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-teal-400"
              required
            />

          </div>

          <div>

            <label
              for="cantidad-personas"
              class="mb-2 block text-sm text-slate-300"
            >
              Cantidad de personas
            </label>

            <input
              id="cantidad-personas"
              type="number"
              min="1"
              placeholder="Ej: 4"
              class="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-teal-400"
              required
            />

          </div>

          <div>

            <label
              for="cantidad-equipos"
              class="mb-2 block text-sm text-slate-300"
            >
              Cantidad de equipos
            </label>

            <input
              id="cantidad-equipos"
              type="number"
              min="0"
              placeholder="Ej: 10"
              class="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-teal-400"
              required
            />

          </div>

          <div>

            <label
              for="temperatura-exterior"
              class="mb-2 block text-sm text-slate-300"
            >
              Temperatura exterior (°C)
            </label>

            <input
              id="temperatura-exterior"
              type="number"
              step="0.1"
              placeholder="Ej: 28"
              class="w-full rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none transition focus:border-teal-400"
              required
            />

          </div>

          <div class="flex items-center gap-3 md:pt-7">

            <input
              id="uso-horario-pico"
              type="checkbox"
              class="h-5 w-5 accent-teal-400"
            />

            <label
              for="uso-horario-pico"
              class="text-sm text-slate-300"
            >
              Uso de equipos en horario pico (7pm - 11pm)
            </label>

          </div>

          <div class="flex flex-col gap-3 md:col-span-2">

            <button
              id="analizar-btn"
              type="submit"
              class="w-full rounded-lg bg-teal-400 px-6 py-3 font-semibold text-slate-950 transition hover:bg-teal-300 disabled:cursor-not-allowed disabled:opacity-60"
            >
              Analizar consumo
            </button>

            <button
              id="limpiar-btn"
              type="button"
              class="w-full rounded-lg border border-slate-700 bg-slate-800 px-6 py-3 font-semibold text-slate-300 transition hover:bg-slate-700"
            >
              Limpiar
            </button>

          </div>

        </form>

        <div
          id="resultado"
          class="mt-8 hidden"
        ></div>

      </div>

    </section>

    <section
      id="seccion-consultas"
      class="mx-auto hidden max-w-6xl px-6 py-12"
    >

      <div class="mb-10">

        <p class="mb-2 text-sm font-semibold uppercase tracking-wider text-teal-400">
          Consultas
        </p>

        <h2 class="text-4xl font-bold">
          Consultá tus análisis
        </h2>

        <p class="mt-3 max-w-2xl text-slate-400">
          Buscá análisis existentes por número de análisis o por usuario.
        </p>

      </div>

      <div class="grid gap-6 md:grid-cols-2">

        <div class="rounded-2xl border border-slate-800 bg-slate-900 p-6">

          <h3 class="mb-2 text-xl font-semibold">
            Buscar por número de análisis
          </h3>

          <p class="mb-5 text-sm text-slate-400">
            Ingresá el número del análisis que querés consultar.
          </p>

          <form
            id="form-consulta-id"
            class="flex gap-3"
          >

            <input
              id="consulta-id"
              type="number"
              min="1"
              placeholder="Ej: 15"
              class="min-w-0 flex-1 rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none focus:border-teal-400"
              required
            />

            <button
              id="buscar-id-btn"
              type="submit"
              class="rounded-lg bg-teal-400 px-5 py-3 font-semibold text-slate-950 transition hover:bg-teal-300 disabled:opacity-60"
            >
              Buscar
            </button>

          </form>

        </div>

        <div class="rounded-2xl border border-slate-800 bg-slate-900 p-6">

          <h3 class="mb-2 text-xl font-semibold">
            Buscar por número de cliente
          </h3>

          <p class="mb-5 text-sm text-slate-400">
            Ingresá el ID del usuario para consultar sus análisis.
          </p>

          <form
            id="form-consulta-usuario"
            class="flex gap-3"
          >

            <input
              id="consulta-usuario"
              type="number"
              min="1"
              placeholder="Ej: 4"
              class="min-w-0 flex-1 rounded-lg border border-slate-700 bg-slate-800 px-4 py-3 text-white outline-none focus:border-teal-400"
              required
            />

            <button
              id="buscar-usuario-btn"
              type="submit"
              class="rounded-lg bg-teal-400 px-5 py-3 font-semibold text-slate-950 transition hover:bg-teal-300 disabled:opacity-60"
            >
              Buscar
            </button>

          </form>

        </div>

      </div>

      <div
        id="resultado-consulta"
        class="mt-8 hidden"
      ></div>

    </section>

  </main>
`

const navNuevo = document.querySelector('#nav-nuevo')
const navConsultas = document.querySelector('#nav-consultas')

const seccionNuevo = document.querySelector('#seccion-nuevo')
const seccionConsultas = document.querySelector('#seccion-consultas')

const formulario = document.querySelector('#analisis-form')
const botonAnalizar = document.querySelector('#analizar-btn')
const botonLimpiar = document.querySelector('#limpiar-btn')
const resultado = document.querySelector('#resultado')

const formConsultaId = document.querySelector('#form-consulta-id')
const formConsultaUsuario = document.querySelector('#form-consulta-usuario')

const buscarIdBtn = document.querySelector('#buscar-id-btn')
const buscarUsuarioBtn = document.querySelector('#buscar-usuario-btn')

const inputConsultaId = document.querySelector('#consulta-id')
const inputConsultaUsuario = document.querySelector('#consulta-usuario')

const resultadoConsulta = document.querySelector('#resultado-consulta')

function mostrarSeccion(seccion) {

    const mostrarNuevo = seccion === 'nuevo'

    seccionNuevo.classList.toggle('hidden', !mostrarNuevo)
    seccionConsultas.classList.toggle('hidden', mostrarNuevo)

    navNuevo.classList.toggle('bg-teal-400', mostrarNuevo)
    navNuevo.classList.toggle('text-slate-950', mostrarNuevo)
    navNuevo.classList.toggle('text-slate-300', !mostrarNuevo)

    navConsultas.classList.toggle('bg-teal-400', !mostrarNuevo)
    navConsultas.classList.toggle('text-slate-950', !mostrarNuevo)
    navConsultas.classList.toggle('text-slate-300', mostrarNuevo)
}

function obtenerEstiloCategoria(categoria) {

    const categoriaNormalizada =
        String(categoria ?? '')
            .trim()
            .toUpperCase()

    const estilos = {
        EFICIENTE:
            'w-fit rounded-full bg-green-400/15 px-3 py-1 text-sm font-semibold text-green-400',

        INEFICIENTE:
            'w-fit rounded-full bg-red-400/15 px-3 py-1 text-sm font-semibold text-red-400',

        MODERADO:
            'w-fit rounded-full bg-yellow-400/15 px-3 py-1 text-sm font-semibold text-yellow-400'
    }

    return estilos[categoriaNormalizada] ??
        'w-fit rounded-full bg-slate-400/15 px-3 py-1 text-sm font-semibold text-slate-400'
}

function formatearNumero(valor) {

    if (valor === null || valor === undefined) {
        return '-'
    }

    return Number(valor).toLocaleString(
        'es-AR',
        {
            minimumFractionDigits: 0,
            maximumFractionDigits: 2
        }
    )
}

function formatearProbabilidad(valor) {

    if (valor === null || valor === undefined) {
        return '-'
    }

    const numero = Number(valor)

    if (numero >= 0 && numero <= 1) {
        return `${(numero * 100).toFixed(2)}%`
    }

    return `${numero.toFixed(2)}%`
}

function crearTarjetaAnalisis(analisis) {

    const recomendaciones = analisis.recomendaciones ?? []

    const recomendacionesHtml =
        recomendaciones.length > 0
            ? `
              <div class="mt-6">

                <h4 class="mb-3 font-semibold">
                  Recomendaciones
                </h4>

                <ul class="space-y-2">

                  ${recomendaciones
                .map(
                    recomendacion => `
                          <li class="rounded-lg bg-slate-800 p-3 text-sm text-slate-300">
                            ${recomendacion}
                          </li>
                        `
                )
                .join('')}

                </ul>

              </div>
            `
            : ''

    return `
      <article class="rounded-2xl border border-slate-700 bg-slate-900 p-6">

        <div class="mb-6 flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">

          <div>

            <p class="text-sm text-slate-400">
              Número del análisis
            </p>

            <h3 class="text-2xl font-bold">
              #${analisis.id ?? '-'}
            </h3>

          </div>

          <span class="${obtenerEstiloCategoria(analisis.categoria)}">
            ${analisis.categoria ?? 'Sin categoría'}
          </span>

        </div>

        <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">

          <div class="rounded-lg bg-slate-800 p-4">

            <p class="text-xs text-slate-400">
              Probabilidad
            </p>

            <p class="mt-1 text-lg font-semibold">
              ${formatearProbabilidad(analisis.probabilidad)}
            </p>

          </div>

          <div class="rounded-lg bg-slate-800 p-4">

            <p class="text-xs text-slate-400">
              Costo mensual
            </p>

            <p class="mt-1 text-lg font-semibold">
              $${formatearNumero(analisis.costo_estimado_mensual)}
            </p>

          </div>

          <div class="rounded-lg bg-slate-800 p-4">

            <p class="text-xs text-slate-400">
              Ahorro mensual
            </p>

            <p class="mt-1 text-lg font-semibold">
              $${formatearNumero(analisis.ahorro_potencial_mensual)}
            </p>

          </div>

          <div class="rounded-lg bg-slate-800 p-4">

            <p class="text-xs text-slate-400">
              Ahorro anual
            </p>

            <p class="mt-1 text-lg font-semibold">
              $${formatearNumero(analisis.ahorro_potencial_anual)}
            </p>

          </div>

        </div>

        ${recomendacionesHtml}

      </article>
    `
}

function mostrarError(contenedor, mensaje) {

    contenedor.innerHTML = `
      <div class="rounded-xl border border-red-500/50 bg-red-950/40 p-6">

        <h3 class="mb-2 text-xl font-bold text-red-400">
          No se pudo realizar la consulta
        </h3>

        <p class="text-sm text-red-200">
          ${mensaje}
        </p>

      </div>
    `

    contenedor.classList.remove('hidden')
}

function limpiarResultadoConsulta() {

    resultadoConsulta.innerHTML = ''
    resultadoConsulta.classList.add('hidden')
}

function limpiarNuevoAnalisis() {

    formulario.reset()
    resultado.innerHTML = ''
    resultado.classList.add('hidden')
}

function mostrarCargandoAnalisis() {

    resultado.classList.remove('hidden')

    resultado.innerHTML = `
      <div class="rounded-xl border border-slate-700 bg-slate-900 p-6">

        <p class="text-slate-400">
          Analizando consumo...
        </p>

      </div>
    `
}

function mostrarCargandoConsulta(mensaje) {

    resultadoConsulta.classList.remove('hidden')

    resultadoConsulta.innerHTML = `
      <div class="rounded-xl border border-slate-700 bg-slate-900 p-6">

        <p class="text-slate-400">
          ${mensaje}
        </p>

      </div>
    `
}

async function realizarAnalisis(datos) {

    const response = await fetch(
        `${API_URL}/analisis`,
        {
            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify(datos)
        }
    )

    if (!response.ok) {
        throw new Error(`Error HTTP: ${response.status}`)
    }

    return response.json()
}

async function consultarAnalisisPorId(id) {

    const response = await fetch(
        `${API_URL}/analisis/${id}`
    )

    if (!response.ok) {

        if (response.status === 404) {
            throw new Error(
                'No se encontró un análisis con ese ID.'
            )
        }

        throw new Error(
            `Error HTTP: ${response.status}`
        )
    }

    return response.json()
}

async function consultarAnalisisPorUsuario(usuarioId) {

    const response = await fetch(
        `${API_URL}/analisis/usuario/${usuarioId}`
    )

    if (!response.ok) {

        if (response.status === 404) {
            throw new Error(
                'No se encontraron análisis para ese usuario.'
            )
        }

        throw new Error(
            `Error HTTP: ${response.status}`
        )
    }

    return response.json()
}

function obtenerDatosFormulario() {

    return {
        usuario_id: Number(
            document.querySelector('#usuario-id').value
        ),

        consumo_kwh: Number(
            document.querySelector('#consumo-kwh').value
        ),

        cantidad_personas: Number(
            document.querySelector('#cantidad-personas').value
        ),

        cantidad_equipos: Number(
            document.querySelector('#cantidad-equipos').value
        ),

        temperatura_exterior: Number(
            document.querySelector('#temperatura-exterior').value
        ),

        uso_horario_pico:
        document.querySelector('#uso-horario-pico').checked
    }
}

function mostrarResultadosUsuario(analisisList, usuarioId) {

    if (
        !Array.isArray(analisisList) ||
        analisisList.length === 0
    ) {

        resultadoConsulta.innerHTML = `
          <div class="rounded-xl border border-slate-700 bg-slate-900 p-6">

            <h3 class="mb-2 text-xl font-semibold">
              Sin resultados
            </h3>

            <p class="text-sm text-slate-400">
              No hay análisis registrados para el usuario #${usuarioId}.
            </p>

          </div>
        `

        return
    }

    resultadoConsulta.innerHTML = `
      <div class="mb-6">

        <h3 class="text-xl font-semibold">
          Análisis del usuario #${usuarioId}
        </h3>

        <p class="mt-1 text-sm text-slate-400">
          ${analisisList.length}
          ${analisisList.length === 1
        ? 'análisis encontrado'
        : 'análisis encontrados'}
        </p>

      </div>

      <div class="space-y-5">

        ${analisisList
        .map(analisis => crearTarjetaAnalisis(analisis))
        .join('')}

      </div>
    `
}

navNuevo.addEventListener('click', () => {
    mostrarSeccion('nuevo')
})

navConsultas.addEventListener('click', () => {
    mostrarSeccion('consultas')
})

botonLimpiar.addEventListener('click', () => {
    limpiarNuevoAnalisis()
})

formulario.addEventListener('submit', async (event) => {

    event.preventDefault()

    const datos = obtenerDatosFormulario()

    botonAnalizar.disabled = true
    botonAnalizar.textContent = 'Analizando...'

    resultado.classList.add('hidden')

    try {

        const resultadoBackend =
            await realizarAnalisis(datos)

        resultado.innerHTML =
            crearTarjetaAnalisis(resultadoBackend)

        resultado.classList.remove('hidden')

    } catch (error) {

        resultado.innerHTML = `
          <div class="rounded-xl border border-red-500/50 bg-red-950/40 p-6">

            <h3 class="mb-2 text-xl font-bold text-red-400">
              No se pudo realizar el análisis
            </h3>

            <p class="text-sm text-red-200">
              Verificá que el backend de EnergiAI esté funcionando.
            </p>

          </div>
        `

        resultado.classList.remove('hidden')

    } finally {

        botonAnalizar.disabled = false
        botonAnalizar.textContent = 'Analizar consumo'

    }
})

inputConsultaId.addEventListener('input', () => {

    limpiarResultadoConsulta()

    if (inputConsultaId.value !== '') {
        inputConsultaUsuario.value = ''
    }
})

inputConsultaUsuario.addEventListener('input', () => {

    limpiarResultadoConsulta()

    if (inputConsultaUsuario.value !== '') {
        inputConsultaId.value = ''
    }
})

formConsultaId.addEventListener(
    'submit',
    async (event) => {

        event.preventDefault()

        const id =
            Number(inputConsultaId.value)

        if (!id || id < 1) {
            return
        }

        buscarIdBtn.disabled = true
        buscarIdBtn.textContent = 'Buscando...'

        mostrarCargandoConsulta(
            `Buscando análisis #${id}...`
        )

        try {

            const analisis =
                await consultarAnalisisPorId(id)

            resultadoConsulta.innerHTML = `
              <div class="mb-4">

                <h3 class="text-xl font-semibold">
                  Resultado de la consulta
                </h3>

              </div>

              ${crearTarjetaAnalisis(analisis)}
            `

        } catch (error) {

            mostrarError(
                resultadoConsulta,
                error.message
            )

        } finally {

            buscarIdBtn.disabled = false
            buscarIdBtn.textContent = 'Buscar'

        }
    }
)

formConsultaUsuario.addEventListener(
    'submit',
    async (event) => {

        event.preventDefault()

        const usuarioId =
            Number(inputConsultaUsuario.value)

        if (!usuarioId || usuarioId < 1) {
            return
        }

        buscarUsuarioBtn.disabled = true
        buscarUsuarioBtn.textContent = 'Buscando...'

        mostrarCargandoConsulta(
            `Buscando análisis del usuario #${usuarioId}...`
        )

        try {

            const analisisList =
                await consultarAnalisisPorUsuario(usuarioId)

            mostrarResultadosUsuario(
                analisisList,
                usuarioId
            )

        } catch (error) {

            mostrarError(
                resultadoConsulta,
                error.message
            )

        } finally {

            buscarUsuarioBtn.disabled = false
            buscarUsuarioBtn.textContent = 'Buscar'

        }
    }
)