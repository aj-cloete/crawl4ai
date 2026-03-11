

--- SOURCE: https://docs.getdbt.com/reference/references-overview ---

[Skip to main content](https://docs.getdbt.com/reference/references-overview#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Freferences-overview+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Freferences-overview+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Freferences-overview+so+I+can+ask+questions+about+it.)
The References section contains reference materials for developing with dbt, which includes dbt and dbt Core.
Learn how to add more configurations to your dbt project or adapter, use properties for extra ability, refer to dbt commands, use powerful Jinja functions to streamline your dbt project, and understand how to use dbt artifacts.
#### [Project configurations Customize and configure your dbt project to optimize performance.](https://docs.getdbt.com/reference/dbt_project.yml)
#### [Platform-specific configurations Learn how to optimize performance with data platform-specific configurations in dbt and dbt Core.](https://docs.getdbt.com/reference/resource-configs)
#### [Resource configurations and properties Properties and configurations that provide extra abilities to your projects resources.](https://docs.getdbt.com/reference/configs-and-properties)
#### [dbt Commands Outlines the commands supported by dbt and their relevant flags.](https://docs.getdbt.com/reference/dbt-commands)
#### [dbt Jinja functions and context variables Additional functions and variables to the Jinja context that are useful when working with a dbt project.](https://docs.getdbt.com/reference/dbt-jinja-functions-context-variables)
#### [dbt Artifacts Information on dbt-generated Artifacts and how you can use them.](https://docs.getdbt.com/reference/artifacts/dbt-artifacts)
#### [Snowflake permissions artifacts Provides an example Snowflake database role permissions.](https://docs.getdbt.com/reference/database-permissions/snowflake-permissions)
#### [Databricks permissions artifacts Provides an example Databricks database role permissions.](https://docs.getdbt.com/reference/database-permissions/databricks-permissions)
#### [Redshift permissions artifacts Provides an example Redshift database role permissions.](https://docs.getdbt.com/reference/database-permissions/redshift-permissions)
#### [Postgres permissions artifacts Provides an example Postgres database role permissions.](https://docs.getdbt.com/reference/database-permissions/postgres-permissions)
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/dbt-artifacts ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fdbt-artifacts+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fdbt-artifacts+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fdbt-artifacts+so+I+can+ask+questions+about+it.)
On this page
With every invocation, dbt generates and saves one or more _artifacts_. Several of these are JSON`semantic_manifest.json`, `manifest.json`, `catalog.json`, `run_results.json`, and `sources.json`) that are used to power:
  * [visualizing source freshness](https://docs.getdbt.com/docs/build/sources#source-data-freshness)


They could also be used to:
  * gain insights into your [Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)
  * calculate project-level test coverage
  * perform longitudinal analysis of run timing
  * identify historical changes in table
  * do much, much more


### When are artifacts produced? [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#when-are-artifacts-produced- "Direct link to when-are-artifacts-produced-")
Most dbt commands (and corresponding RPC methods) produce artifacts:
  * [semantic manifest](https://docs.getdbt.com/reference/artifacts/sl-manifest): produced whenever your dbt project is parsed
  * [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json): produced by commands that read and understand your project
  * [run results](https://docs.getdbt.com/reference/artifacts/run-results-json): produced by commands that run, compile, or catalog nodes in your DAG
  * [catalog](https://docs.getdbt.com/reference/artifacts/catalog-json): produced by `docs generate`
  * [sources](https://docs.getdbt.com/reference/artifacts/sources-json): produced by `source freshness`


When running commands from the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation), all artifacts are downloaded by default. If you want to change this behavior, refer to [How to skip artifacts from being downloaded](https://docs.getdbt.com/docs/cloud/configure-cloud-cli#how-to-skip-artifacts-from-being-downloaded).
## Where are artifacts produced?[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#where-are-artifacts-produced "Direct link to Where are artifacts produced?")
By default, artifacts are written to the `/target` directory of your dbt project. You can configure the location using the [`target-path` flag](https://docs.getdbt.com/reference/global-configs/json-artifacts).
## Common metadata[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#common-metadata "Direct link to Common metadata")
All artifacts produced by dbt include a `metadata` dictionary with these properties:
  * `dbt_version`: Version of dbt that produced this artifact. For details about release versioning, refer to [Versioning](https://docs.getdbt.com/reference/commands/version#versioning).
  * `dbt_schema_version`: URL of this artifact's schema. See notes below.
  * `generated_at`: Timestamp in UTC when this artifact was produced.
  * `adapter_type`: The adapter (database), e.g. `postgres`, `spark`, etc.
  * `env`: Any environment variables prefixed with `DBT_ENV_CUSTOM_ENV_` will be included in a dictionary, with the prefix-stripped variable name as its key.
  * [`invocation_id`](https://docs.getdbt.com/reference/dbt-jinja-functions/invocation_id): Unique identifier for this dbt invocation


In the manifest, the `metadata` may also include:
  * `send_anonymous_usage_stats`: Whether this invocation sent [anonymous usage statistics](https://docs.getdbt.com/reference/global-configs/usage-stats) while executing.
  * `project_name`: The `name` defined in the root project's `dbt_project.yml`. (Added in manifest v10 / dbt Core v1.6)
  * `project_id`: Project identifier, hashed from `project_name`, sent with anonymous usage stats if enabled.
  * `user_id`: User identifier, stored by default in `~/dbt/.user.yml`, sent with anonymous usage stats if enabled.


#### Notes:[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#notes "Direct link to Notes:")
  * The structure of dbt artifacts is canonized by [JSON schemas](https://json-schema.org/), which are hosted at [schemas.getdbt.com](https://schemas.getdbt.com/).
  * Artifact versions may change in any minor version of dbt (`v1.x.0`). Each artifact is versioned independently.


## Related docs[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#related-docs "Direct link to Related docs")
  * [Other artifacts](https://docs.getdbt.com/reference/artifacts/other-artifacts) files such as `index.html` or `graph_summary.json`.


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [When are artifacts produced? ](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#when-are-artifacts-produced)[Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#when-are-artifacts-produced- "Direct link to when-are-artifacts-produced-")
  * [Where are artifacts produced?](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#where-are-artifacts-produced)[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#where-are-artifacts-produced "Direct link to Where are artifacts produced?")
  * [Was this page helpful?](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions-context-variables ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions-context-variables#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
## [📄️ adapter Wrap the internal database adapter with the Jinja object `adapter`.](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter)## [📄️ as_bool Use this filter to coerce a Jinja output into boolean value.](https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool)## [📄️ as_native Use this filter to coerce Jinja-compiled output into its native python.](https://docs.getdbt.com/reference/dbt-jinja-functions/as_native)## [📄️ as_number Use this filter to convert Jinja-compiled output to a numeric value..](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number)## [📄️ builtins Read this guide to understand the builtins Jinja variable in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/builtins)## [📄️ config Read this guide to understand the config Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/config)## [📄️ cross-database macros Read this guide to understand cross-database macros in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros)## [📄️ dbt_project.yml context The context methods and variables available when configuring resources in the dbt_project.yml file.](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-project-yml-context)## [📄️ dbt_version Read this guide to understand the dbt_version Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt_version)## [📄️ debug The `{{ debug() }}` macro will open an iPython debugger.](https://docs.getdbt.com/reference/dbt-jinja-functions/debug-method)## [📄️ dispatch dbt extends functionality across data platforms using multiple dispatch.](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch)## [📄️ doc Use the `doc` to reference docs blocks in description fields.](https://docs.getdbt.com/reference/dbt-jinja-functions/doc)## [📄️ env_var Incorporate environment variables using `en_var` function.](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var)## [📄️ exceptions Raise warnings/errors with the `exceptions` namespace.](https://docs.getdbt.com/reference/dbt-jinja-functions/exceptions)## [📄️ execute Use `execute` to return True when dbt is in 'execute' mode.](https://docs.getdbt.com/reference/dbt-jinja-functions/execute)## [📄️ flags The `flags` variable contains values of flags provided on the cli.](https://docs.getdbt.com/reference/dbt-jinja-functions/flags)## [📄️ fromjson Deserialize a JSON string into python with `fromjson` context method.](https://docs.getdbt.com/reference/dbt-jinja-functions/fromjson)## [📄️ fromyaml Deserialize a YAML string into python with `fromyaml` context method.](https://docs.getdbt.com/reference/dbt-jinja-functions/fromyaml)## [📄️ graph The `graph` context variable contains info about nodes in your project.](https://docs.getdbt.com/reference/dbt-jinja-functions/graph)## [📄️ invocation_id The `invocation_id` outputs a UUID generated for this dbt command.](https://docs.getdbt.com/reference/dbt-jinja-functions/invocation_id)## [📄️ local_md5 Calculate an MD5 hash of a string with `local_md5` context variable.](https://docs.getdbt.com/reference/dbt-jinja-functions/local_md5)## [📄️ log Learn more about the log Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/log)## [📄️ model `model` is the dbt graph object (or node) for the current model.](https://docs.getdbt.com/reference/dbt-jinja-functions/model)## [📄️ modules `modules` Jinja variables has useful Python modules to operate data.](https://docs.getdbt.com/reference/dbt-jinja-functions/modules)## [📄️ on-run-end context Use these variables in the context for `on-run-end` hooks.](https://docs.getdbt.com/reference/dbt-jinja-functions/on-run-end-context)## [📄️ packages.yml context Use these context methods to configure dependencies in the packages.yml file.](https://docs.getdbt.com/reference/dbt-jinja-functions/packages.yml%20context)## [📄️ print Use the `print()` to print messages to the log file and stdout.](https://docs.getdbt.com/reference/dbt-jinja-functions/print)## [📄️ profiles.yml context Use these context methods to configure resources in `profiles.yml` file.](https://docs.getdbt.com/reference/dbt-jinja-functions/profiles-yml-context)## [📄️ project_name Read this guide to understand the project_name Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/project_name)## [📄️ properties.yml context The context methods and variables available when configuring resources in a properties.yml file.](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-properties-yml-context)## [📄️ ref Read this guide to understand the ref Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/ref)## [📄️ return Read this guide to understand the return Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/return)## [📄️ run_query Use `run_query` macro to run queries and fetch results.](https://docs.getdbt.com/reference/dbt-jinja-functions/run_query)## [📄️ run_started_at Use `run_started_at` to output the timestamp the run started.](https://docs.getdbt.com/reference/dbt-jinja-functions/run_started_at)## [📄️ schema The schema that the model is configured to be materialized in.](https://docs.getdbt.com/reference/dbt-jinja-functions/schema)## [📄️ schemas A list of schemas where dbt built objects during the current run.](https://docs.getdbt.com/reference/dbt-jinja-functions/schemas)## [📄️ selected_resources Contains a list of all the nodes selected by current dbt command.](https://docs.getdbt.com/reference/dbt-jinja-functions/selected_resources)## [📄️ set Converts any iterable to a sequence of iterable and unique elements.](https://docs.getdbt.com/reference/dbt-jinja-functions/set)## [📄️ source Read this guide to understand the source Jinja function in dbt.](https://docs.getdbt.com/reference/dbt-jinja-functions/source)## [📄️ statement blocks SQL queries that hit database and return results to your Jinja context.](https://docs.getdbt.com/reference/dbt-jinja-functions/statement-blocks)## [📄️ target The `target` variable contains information about your connection to the warehouse.](https://docs.getdbt.com/reference/dbt-jinja-functions/target)## [📄️ this Represents the current model in the database.](https://docs.getdbt.com/reference/dbt-jinja-functions/this)## [📄️ thread_id The `thread_id` outputs an identifier for the current Python thread.](https://docs.getdbt.com/reference/dbt-jinja-functions/thread_id)## [📄️ tojson Use this context method to serialize a Python object primitive.](https://docs.getdbt.com/reference/dbt-jinja-functions/tojson)## [📄️ toyaml Used to serialize a Python object primitive.](https://docs.getdbt.com/reference/dbt-jinja-functions/toyaml)## [📄️ var Pass variables from `dbt_project.yml` file into models.](https://docs.getdbt.com/reference/dbt-jinja-functions/var)## [📄️ zip Use this context method to return an iterator of tuples.](https://docs.getdbt.com/reference/dbt-jinja-functions/zip)
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/resource-configs/resource-path ---

[Skip to main content](https://docs.getdbt.com/reference/resource-configs/resource-path#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fresource-configs%2Fresource-path+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fresource-configs%2Fresource-path+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fresource-configs%2Fresource-path+so+I+can+ask+questions+about+it.)
On this page
The `<resource-path>` nomenclature is used in this documentation when documenting how to configure resource types like models, seeds, snapshots, tests, sources, and others, from your `dbt_project.yml` file.
It represents the nested dictionary keys that provide the path to a directory of that resource type, or a single instance of that resource type by name.
```
resource_type:project_name:directory_name:subdirectory_name:instance_of_resource_type (by name):
```

## Example[​](https://docs.getdbt.com/reference/resource-configs/resource-path#example "Direct link to Example")
The following examples are mostly for models and a source, but the same concepts apply for seeds, snapshots, tests, sources, and other resource types.
### Apply config to all models[​](https://docs.getdbt.com/reference/resource-configs/resource-path#apply-config-to-all-models "Direct link to Apply config to all models")
To apply a configuration to all models, do not use a `<resource-path>`:
dbt_project.yml
```
models:+enabled:false# this will disable all models (not a thing you probably want to do)
```

### Apply config to all models in your project[​](https://docs.getdbt.com/reference/resource-configs/resource-path#apply-config-to-all-models-in-your-project "Direct link to Apply config to all models in your project")
To apply a configuration to all models in _your_ project only, use your [project name](https://docs.getdbt.com/reference/project-configs/name) as the `<resource-path>`:
dbt_project.yml
```
name: jaffle_shopmodels:jaffle_shop:+enabled:false# this will apply to all models in your project, but not any installed packages
```

### Apply config to all models in a subdirectory[​](https://docs.getdbt.com/reference/resource-configs/resource-path#apply-config-to-all-models-in-a-subdirectory "Direct link to Apply config to all models in a subdirectory")
To apply a configuration to all models in a subdirectory of your project, e.g. `staging`, nest the directory under the project name:
dbt_project.yml
```
name: jaffle_shopmodels:jaffle_shop:staging:+enabled:false# this will apply to all models in the `staging/` directory of your project
```

In the following project, this would apply to models in the `staging/` directory, but not the `marts/` directory:
```
├── dbt_project.yml└── models    ├── marts    └── staging
```

### Apply config to a specific model[​](https://docs.getdbt.com/reference/resource-configs/resource-path#apply-config-to-a-specific-model "Direct link to Apply config to a specific model")
To apply a configuration to a specific model, nest the full path under the project name. For a model at `/staging/stripe/payments.sql`, this would look like:
dbt_project.yml
```
name: jaffle_shopmodels:jaffle_shop:staging:stripe:payments:+enabled:false# this will apply to only one model
```

In the following project, this would only apply to the `payments` model:
```
├── dbt_project.yml└── models    ├── marts    │   └── core    │       ├── dim_customers.sql    │       └── fct_orders.sql    └── staging        ├── jaffle_shop        │   ├── customers.sql        │   └── orders.sql        └── stripe            └── payments.sql
```

### Apply config to a source nested in a subfolder[​](https://docs.getdbt.com/reference/resource-configs/resource-path#apply-config-to-a-source-nested-in-a-subfolder "Direct link to Apply config to a source nested in a subfolder")
To disable a source table nested in a YAML file in a subfolder, you will need to supply the subfolder(s) within the path to that YAML file, as well as the source name and the table name in the `dbt_project.yml` file. The following example shows how to disable a source table nested in a YAML file in a subfolder:
dbt_project.yml
```
sources:your_project_name:subdirectory_name:source_name:source_table_name:+enabled:false
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-commands ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-commands#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-commands+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-commands+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-commands+so+I+can+ask+questions+about+it.)
On this page
You can run dbt using the following tools:
  * In your browser with the [Studio IDE](https://docs.getdbt.com/docs/cloud/studio-ide/develop-in-studio)
  * On the command line interface using the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation) or open-source [dbt Core](https://docs.getdbt.com/docs/local/install-dbt).


A key distinction with the tools mentioned, is that dbt CLI and Studio IDE are designed to support safe parallel execution of dbt commands, leveraging dbt's infrastructure and its comprehensive [features](https://docs.getdbt.com/docs/cloud/about-cloud/dbt-cloud-features). In contrast, dbt Core _doesn't support_ safe parallel execution for multiple invocations in the same process. Learn more in the [parallel execution](https://docs.getdbt.com/reference/dbt-commands#parallel-execution) section.
## Parallel execution[​](https://docs.getdbt.com/reference/dbt-commands#parallel-execution "Direct link to Parallel execution")
dbt allows for concurrent execution of commands, enhancing efficiency without compromising data integrity. This enables you to run multiple commands at the same time. However, it's important to understand which commands can be run in parallel and which can't.
In contrast, [`dbt-core` _doesn't_ support](https://docs.getdbt.com/reference/programmatic-invocations#parallel-execution-not-supported) safe parallel execution for multiple invocations in the same process, and requires users to manage concurrency manually to ensure data integrity and system stability.
To ensure your dbt workflows are both efficient and safe, you can run different types of dbt commands at the same time (in parallel) — for example, `dbt build` (write operation) can safely run alongside `dbt parse` (read operation) at the same time. However, you can't run `dbt build` and `dbt run` (both write operations) at the same time.
dbt commands can be `read` or `write` commands:
Command type | Description | Example
---|---|---
**Write** | These commands perform actions that change data or metadata in your data platform. Limited to one invocation at any given time, which prevents any potential conflicts, such as overwriting the same table in your data platform at the same time. |  `dbt build``dbt run`
**Read** | These commands involve operations that fetch or read data without making any changes to your data platform. Can have multiple invocations in parallel and aren't limited to one invocation at any given time. This means read commands can run in parallel with other read commands and a single write command. |  `dbt parse``dbt compile`
Loading table...
---
## Available commands[​](https://docs.getdbt.com/reference/dbt-commands#available-commands "Direct link to Available commands")
The following sections outline the commands supported by dbt and their relevant flags. They are available in all tools and all [supported versions](https://docs.getdbt.com/docs/dbt-versions/core) unless noted otherwise. You can run these commands in your specific tool by prefixing them with `dbt` — for example, to run the `test` command, type `dbt test`.
For information about selecting models on the command line, refer to [Model selection syntax](https://docs.getdbt.com/reference/node-selection/syntax).
Commands with a ('❌') indicate write commands, commands with a ('✅') indicate read commands, and commands with a (N/A) indicate it's not relevant to the parallelization of dbt commands.
Some commands are not yet supported in the dbt Fusion engine or have limited functionality. See the [Fusion supported features](https://docs.getdbt.com/docs/fusion/supported-features) page for details.
Command | Description | Parallel execution | Caveats
---|---|---|---
Builds and tests all selected resources (models, seeds, tests, and more) | ❌ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
cancel | Cancels the most recent invocation. | N/A |  dbt CLI Requires [dbt v1.6 or higher](https://docs.getdbt.com/docs/dbt-versions/core)
Deletes artifacts present in the dbt project | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Clones selected models from the specified state | ❌ | All tools Requires [dbt v1.6 or higher](https://docs.getdbt.com/docs/dbt-versions/core)
Compiles (but does not run) the models in a project | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Debugs dbt connections and projects | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Downloads dependencies for a project | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Generates documentation for a project | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core) Not yet supported in Fusion
Enables you to interact with your dbt environment. | N/A |  dbt CLI Requires [dbt v1.5 or higher](https://docs.getdbt.com/docs/dbt-versions/core)
help | Displays help information for any command | N/A |  dbt Core, dbt CLI All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Initializes a new dbt project | ✅ |  Fusion dbt Core All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Enables users to debug long-running sessions by interacting with active invocations. | N/A |  dbt CLI Requires [dbt v1.5 or higher](https://docs.getdbt.com/docs/dbt-versions/core)
Lists resources defined in a dbt project | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Parses a project and writes detailed timing info | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
reattach | Reattaches to the most recent invocation to retrieve logs and artifacts. | N/A |  dbt CLI Requires [dbt v1.6 or higher](https://docs.getdbt.com/docs/dbt-versions/core)
Retry the last run `dbt` command from the point of failure | ✅ | All tools Requires [dbt v1.6 or higher](https://docs.getdbt.com/docs/dbt-versions/core)
Runs the models in a project | ❌ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Invokes a macro, including running arbitrary maintenance SQL against the database | ❌ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Loads CSV files into the database | ❌ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Previews table rows post-transformation | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Executes "snapshot" jobs defined in a project | ❌ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Provides tools for working with source data (including validating that sources are "fresh") | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core)
Executes tests defined in a project | ✅ | All tools All [supported versions](https://docs.getdbt.com/docs/dbt-versions/core) Fusion flag `--warn-error` not yet supported
Loading table...
---
Note, use the [`--version`](https://docs.getdbt.com/reference/commands/version) flag to display the installed dbt Core or dbt CLI version. (Not applicable for the Studio IDE). Available on all [supported versions](https://docs.getdbt.com/docs/dbt-versions/core).
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/database-permissions/databricks-permissions ---

[Skip to main content](https://docs.getdbt.com/reference/database-permissions/databricks-permissions#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fdatabricks-permissions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fdatabricks-permissions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fdatabricks-permissions+so+I+can+ask+questions+about+it.)
On this page
In Databricks, permissions are used to control who can perform certain actions on different database objects. Use SQL statements to manage permissions in a Databricks database.
## Example Databricks permissions[​](https://docs.getdbt.com/reference/database-permissions/databricks-permissions#example-databricks-permissions "Direct link to Example Databricks permissions")
The following example provides you with the SQL statements you can use to manage permissions.
**Note** that you can grant permissions on `securable_objects` to `principals` (This can be user, service principal, or group). For example, `grant privilege_type` on `securable_object` to `principal`.
```
grant all privileges on schema schema_name to principal;grant create table on schema schema_name to principal;grant create view on schema schema_name to principal;
```

Check out the [official documentation](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/privileges.html#privilege-types-by-securable-object-in-unity-catalog) for more information.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/resource-configs ---

[Skip to main content](https://docs.getdbt.com/reference/resource-configs#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
## [📄️ Microsoft Azure Synapse DWH configurations All configuration options for the Microsoft SQL Server adapter also apply to this adapter.](https://docs.getdbt.com/reference/resource-configs/azuresynapse-configs)## [📄️ Amazon Athena configurations Reference article for the Amazon Athena adapter for dbt Core and the dbt platform.](https://docs.getdbt.com/reference/resource-configs/athena-configs)## [📄️ Cloudera Impala configurations Impala Configs - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/impala-configs)## [📄️ Apache Spark configurations Apache Spark Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/spark-configs)## [📄️ BigQuery configurations Reference guide for Big Query configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/bigquery-configs)## [📄️ ClickHouse configurations Read this guide to understand ClickHouse configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/clickhouse-configs)## [📄️ Databricks configurations Configuring tables](https://docs.getdbt.com/reference/resource-configs/databricks-configs)## [📄️ DeltaStream configurations DeltaStream Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/deltastream-configs)## [📄️ Doris/SelectDB configurations Doris/SelectDB Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/doris-configs)## [📄️ DuckDB configurations Profile](https://docs.getdbt.com/reference/resource-configs/duckdb-configs)## [📄️ Exasol configurations Exasol Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/exasol-configs)## [📄️ Microsoft Fabric Data Warehouse configurations This page describes configuration options specific to the dbt-fabric adapter for Microsoft Fabric Data Warehouse. It outlines supported materializations, incremental strategies (including merge and microbatch), cross-warehouse references, warehouse snapshots, and profile setup.](https://docs.getdbt.com/reference/resource-configs/fabric-configs)## [📄️ Microsoft Fabric Spark configurations Microsoft Fabric Spark Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/fabricspark-configs)## [📄️ Firebolt configurations Setting quote_columns](https://docs.getdbt.com/reference/resource-configs/firebolt-configs)## [📄️ Greenplum configurations Greenplum Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/greenplum-configs)## [📄️ Cloudera Hive configurations Cloudera Hive Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/hive-configs)## [📄️ Infer configurations Read this guide to understand how to configure Infer with dbt.](https://docs.getdbt.com/reference/resource-configs/infer-configs)## [📄️ IBM Netezza configurations Instance requirements](https://docs.getdbt.com/reference/resource-configs/ibm-netezza-config)## [📄️ Materialize configurations Materialize Configurations- Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/materialize-configs)## [📄️ Microsoft SQL Server configurations Materializations](https://docs.getdbt.com/reference/resource-configs/mssql-configs)## [📄️ MindsDB configurations Authentication](https://docs.getdbt.com/reference/resource-configs/mindsdb-configs)## [📄️ Oracle configurations Use parallel hint](https://docs.getdbt.com/reference/resource-configs/oracle-configs)## [📄️ Postgres configurations Postgres Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/postgres-configs)## [📄️ Redshift configurations Redshift Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/redshift-configs)## [📄️ Salesforce Data 360 configurations Salesforce Data 360 Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/data-cloud-configs)## [📄️ SingleStore configurations Incremental materialization strategies](https://docs.getdbt.com/reference/resource-configs/singlestore-configs)## [📄️ Snowflake configurations Snowflake Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/snowflake-configs)## [📄️ Starburst/Trino configurations Cluster requirements](https://docs.getdbt.com/reference/resource-configs/trino-configs)## [📄️ Starrocks configurations Starrocks Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/starrocks-configs)## [📄️ Teradata configurations General](https://docs.getdbt.com/reference/resource-configs/teradata-configs)## [📄️ Upsolver configurations Upsolver Configurations - Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/upsolver-configs)## [📄️ Vertica configurations Configuration of Incremental Models](https://docs.getdbt.com/reference/resource-configs/vertica-configs)## [📄️ IBM watsonx.data Presto configurations Instance requirements](https://docs.getdbt.com/reference/resource-configs/watsonx-presto-config)## [📄️ IBM watsonx.data Spark configurations Instance requirements](https://docs.getdbt.com/reference/resource-configs/watsonx-spark-config)## [📄️ Yellowbrick configurations Yellowbrick Configurations: Read this in-depth guide to learn about configurations in dbt.](https://docs.getdbt.com/reference/resource-configs/yellowbrick-configs)
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/database-permissions/about-database-permissions ---

[Skip to main content](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fabout-database-permissions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fabout-database-permissions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fabout-database-permissions+so+I+can+ask+questions+about+it.)
On this page
Database permissions are access rights and privileges granted to users or roles within a database or data platform. They help you specify what actions users or roles can perform on various database objects, like tables, views, schemas, or even the entire database.
### Why are they useful[​](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#why-are-they-useful "Direct link to Why are they useful")
  * Database permissions are essential for security and data access control.
  * They ensure that only authorized users can perform specific actions.
  * They help maintain data integrity, prevent unauthorized changes, and limit exposure to sensitive data.
  * Permissions also support compliance with data privacy regulations and auditing.


### How to use them[​](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#how-to-use-them "Direct link to How to use them")
  * Users and administrators can grant and manage permissions at various levels (such as table, schema, and so on) using SQL statements or through the database system's interface.
  * Assign permissions to individual users or roles (groups of users) based on their responsibilities.
    * Typical permissions include "SELECT" (read), "INSERT" (add data), "UPDATE" (modify data), "DELETE" (remove data), and administrative rights like "CREATE" and "DROP."
  * Users should be assigned permissions that ensure they have the necessary access to perform their tasks without overextending privileges.


Something to note is that each data platform provider might have different approaches and names for privileges. Refer to their documentation for more details.
### Examples[​](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#examples "Direct link to Examples")
Refer to the following database permission pages for more info on examples and how to set up database permissions:


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/configs-and-properties ---

[Skip to main content](https://docs.getdbt.com/reference/configs-and-properties#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fconfigs-and-properties+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fconfigs-and-properties+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fconfigs-and-properties+so+I+can+ask+questions+about+it.)
Understand the difference between properties and configurations in dbt: properties describe resources, while configurations control how dbt builds them in the warehouse.
Resources in your project—models, snapshots, seeds, tests, and the rest—can have a number of declared _properties_. Resources can also define _configurations_ (configs), which are a special kind of property that bring extra abilities. What's the distinction?
  * Properties are declared for resources one-by-one in `properties.yml` files. Configs can be defined there, nested under a `config` property. They can also be set one-by-one via a `config()` macro (right within `.sql` files), and for many resources at once in `dbt_project.yml`.
  * Because configs can be set in multiple places, they are also applied hierarchically. An individual resource might _inherit_ or _override_ configs set elsewhere.
  * You can select resources based on their config values using the `config:` selection method, but not the values of non-config properties.
  * There are slightly different naming conventions for properties and configs depending on the file type. Refer to [naming convention](https://docs.getdbt.com/reference/dbt_project.yml#naming-convention) for more details.


A rule of thumb: properties declare things _about_ your project resources; configs go the extra step of telling dbt _how_ to build those resources in your warehouse. This is generally true, but not always, so it's always good to check!
For example, you can use resource **properties** to:
  * Describe models, snapshots, seed files, and their columns
  * Assert "truths" about a model, in the form of [data tests](https://docs.getdbt.com/docs/build/data-tests), e.g. "this `id` column is unique"
  * Define official downstream uses of your data models, in the form of [exposures](https://docs.getdbt.com/docs/build/exposures), and assert an exposure's "type"


Whereas you can use **configurations** to:
  * Change how a model will be materialized (table, view, incremental, etc)
  * Declare where a seed will be created in the database (`<database>.<schema>.<alias>`)
  * Declare whether a resource should persist its descriptions as comments in the database
  * Apply tags and meta to a resource


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/database-permissions/postgres-permissions ---

[Skip to main content](https://docs.getdbt.com/reference/database-permissions/postgres-permissions#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fpostgres-permissions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fpostgres-permissions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fpostgres-permissions+so+I+can+ask+questions+about+it.)
On this page
In Postgres, permissions are used to control who can perform certain actions on different database objects. Use SQL statements to manage permissions in a Postgres database.
## Example Postgres permissions[​](https://docs.getdbt.com/reference/database-permissions/postgres-permissions#example-postgres-permissions "Direct link to Example Postgres permissions")
The following example provides you with the SQL statements you can use to manage permissions. These examples allow you to run dbt smoothly without encountering permission issues, such as creating schemas, reading existing data, and accessing the information schema.
**Note** that `database_name`, `source_schema`, `destination_schema`, and `user_name` are placeholders and you can replace them as needed for your organization's naming convention.
```
grantconnectondatabase database_name to user_name;-- Grant read permissions on the source schemagrantusageonschema source_schema to user_name;grantselectonalltablesinschema source_schema to user_name;alterdefaultprivilegesinschema source_schema grantselectontablesto user_name;-- Create destination schema and make user_name the ownercreateschemaifnotexists destination_schema;alterschema destination_schema owner to user_name;-- Grant write permissions on the destination schemagrantusageonschema destination_schema to user_name;grantcreateonschema destination_schema to user_name;grantinsert,update,delete,truncateonalltablesinschema destination_schema to user_name;alterdefaultprivilegesinschema destination_schema grantinsert,update,delete,truncateontablesto user_name;
```

Check out the [official documentation](https://www.postgresql.org/docs/current/sql-grant.html) for more information.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt_project.yml ---

[Skip to main content](https://docs.getdbt.com/reference/dbt_project.yml#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt_project.yml+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt_project.yml+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt_project.yml+so+I+can+ask+questions+about+it.)
On this page
The dbt_project.yml file is a required file for all dbt projects. It contains important information that tells dbt how to operate your project.
Every [dbt project](https://docs.getdbt.com/docs/build/projects) needs a `dbt_project.yml` file — this is how dbt knows a directory is a dbt project. It also contains important information that tells dbt how to operate your project. It works as follows:
  * dbt uses [YAML](https://yaml.org/) in a few different places. If you're new to YAML, it would be worth learning how arrays, dictionaries, and strings are represented.
  * By default, dbt looks for the `dbt_project.yml` in your current working directory and its parents, but you can set a different directory using the `--project-dir` flag or the `DBT_PROJECT_DIR` environment variable.
  * Specify your dbt project ID in the `dbt_project.yml` file using `project-id` under the `dbt-cloud` config. Find your project ID in your dbt project URL: For example, in `https://YOUR_ACCESS_URL/11/projects/123456`, the project ID is `123456`.
  * Note, you can't set up a "property" in the `dbt_project.yml` file if it's not a config (an example is [macros](https://docs.getdbt.com/reference/macro-properties)). This applies to all types of resources. Refer to [Configs and properties](https://docs.getdbt.com/reference/configs-and-properties) for more detail.


## Example[​](https://docs.getdbt.com/reference/dbt_project.yml#example "Direct link to Example")
The following example is a list of all available configurations in the `dbt_project.yml` file:
dbt_project.yml
```
: string: 2: version: profilename: [directorypath]: [directorypath]: [directorypath]: [directorypath]: [directorypath]: [directorypath]: [directorypath]: [directorypath]: [directorypath]: directorypath: [directorypath]: string: version-range | [version-range]:: project_id # Required: environment_id # Optional: account-host # Defaults to 'cloud.getdbt.com'; Required if use a different Access URL:: true | false:database: true | falseschema: true | falseidentifier: true | falsesnowflake_ignore_case: true | false  # Fusion-only config. Aligns with Snowflake's session parameter QUOTED_IDENTIFIERS_IGNORE_CASE behavior. # Ignored by dbt Core and other adapters.metrics:models:seeds:semantic-models:<semantic-model-configs>[](https://docs.getdbt.com/docs/build/semantic-models)saved-queries:<saved-queries-configs>[](https://docs.getdbt.com/docs/build/saved-queries)snapshots:sources:data_tests:: sql-statement | [sql-statement]: sql-statement | [sql-statement]:-macro_namespace: packagenamesearch_order:[packagename]: true | falsefunctions:
```

## The `+` prefix[​](https://docs.getdbt.com/reference/dbt_project.yml#the--prefix "Direct link to the--prefix")
dbt demarcates between a folder name and a configuration by using a `+` prefix before the configuration name. The `+` prefix is used for configs _only_ and applies to `dbt_project.yml` under the corresponding resource key. It doesn't apply to:
  * `config()` Jinja macro within a resource file
  * config property in a `.yml` file.


For more info, see the [Using the `+` prefix](https://docs.getdbt.com/reference/resource-configs/plus-prefix).
## Naming convention[​](https://docs.getdbt.com/reference/dbt_project.yml#naming-convention "Direct link to Naming convention")
It's important to follow the correct YAML naming conventions for the configs in your `dbt_project.yml` file to ensure dbt can process them properly. This is especially true for resource types with more than one word.
  * Use dashes (`-`) when configuring resource types with multiple words in your `dbt_project.yml` file. Here's an example for [saved queries](https://docs.getdbt.com/docs/build/saved-queries#configure-saved-query):
dbt_project.yml
```
saved-queries:# Use dashes for resource types in the dbt_project.yml file.my_saved_query:+cache:enabled:true
```

  * Use underscore (`_`) when configuring resource types with multiple words for YAML files other than the `dbt_project.yml` file. For example, here's the same saved queries resource in the `semantic_models.yml` file:
models/semantic_models.yml
```
saved_queries:# Use underscores everywhere outside the dbt_project.yml file.-name: saved_query_name...# Rest of the saved queries configuration.config:cache:enabled:true
```



## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/database-permissions/redshift-permissions ---

[Skip to main content](https://docs.getdbt.com/reference/database-permissions/redshift-permissions#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fredshift-permissions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fredshift-permissions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fredshift-permissions+so+I+can+ask+questions+about+it.)
On this page
In Redshift, permissions are used to control who can perform certain actions on different database objects. Use SQL statements to manage permissions in a Redshift database.
## Example Redshift permissions[​](https://docs.getdbt.com/reference/database-permissions/redshift-permissions#example-redshift-permissions "Direct link to Example Redshift permissions")
The following example provides you with the SQL statements you can use to manage permissions.
**Note** that `database_name`, `database.schema_name`, and `user_name` are placeholders and you can replace them as needed for your organization's naming convention.
```
grant create schema on database database_name to user_name;grant usage on schema database.schema_name to user_name;grant create table on schema database.schema_name to user_name;grant create view on schema database.schema_name to user_name;grant usage for schemas in database database_name to role role_name;grant select on all tables in database database_name to user_name;grant select on all views in database database_name to user_name;
```

To connect to the database, confirm with an admin that your user role or group has been added to the database. Note that Redshift permissions differ from Postgres, and commands like [`grant connect`](https://www.postgresql.org/docs/current/sql-grant.html) aren't supported in Redshift.
Check out the [official documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_GRANT.html) for more information.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/database-permissions/snowflake-permissions ---

[Skip to main content](https://docs.getdbt.com/reference/database-permissions/snowflake-permissions#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fsnowflake-permissions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fsnowflake-permissions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fsnowflake-permissions+so+I+can+ask+questions+about+it.)
On this page
In Snowflake, permissions are used to control who can perform certain actions on different database objects. Use SQL statements to manage permissions in a Snowflake database.
## Set up Snowflake account[​](https://docs.getdbt.com/reference/database-permissions/snowflake-permissions#set-up-snowflake-account "Direct link to Set up Snowflake account")
This section explains how to set up permissions and roles within Snowflake. In Snowflake, you would perform these actions using SQL commands and set up your data warehouse and access control within Snowflake's ecosystem.
  1. Set up databases


```
use role sysadmin;create database raw;create database analytics;
```

  1. Set up warehouses


```
create warehouse loading    warehouse_size = xsmall    auto_suspend = 3600    auto_resume = false    initially_suspended = true;create warehouse transforming    warehouse_size = xsmall    auto_suspend = 60    auto_resume = true    initially_suspended = true;create warehouse reporting    warehouse_size = xsmall    auto_suspend = 60    auto_resume = true    initially_suspended = true;
```

  1. Set up roles and warehouse permissions


```
use role securityadmin;create role loader;grant all on warehouse loading to role loader; create role transformer;grant all on warehouse transforming to role transformer;create role reporter;grant all on warehouse reporting to role reporter;
```

  1. Create users, assigning them to their roles


Every person and application gets a separate user and is assigned to the correct role.
```
create user stitch_user -- or fivetran_user    password = '_generate_this_'    default_warehouse = loading    default_role = loader; create user claire -- or amy, jeremy, etc.    password = '_generate_this_'    default_warehouse = transforming    default_role = transformer    must_change_password = true;create user dbt_cloud_user    password = '_generate_this_'    default_warehouse = transforming    default_role = transformer;create user looker_user -- or mode_user etc.    password = '_generate_this_'    default_warehouse = reporting    default_role = reporter;-- then grant these roles to each usergrant role loader to user stitch_user; -- or fivetran_usergrant role transformer to user dbt_cloud_user;grant role transformer to user claire; -- or amy, jeremygrant role reporter to user looker_user; -- or mode_user, periscope_user
```

  1. Let loader load data


Give the role unilateral permission to operate on the raw database
```
use role sysadmin;grant all on database raw to role loader;
```

  1. Let transformer transform data


The transformer role needs to be able to read raw data.
If you do this before you have any data loaded, you can run:
```
grant usage on database raw to role transformer;grant usage on future schemas in database raw to role transformer;grant select on future tables in database raw to role transformer;grant select on future views in database raw to role transformer;
```

If you already have data loaded in the raw database, make sure also you run the following to update the permissions
```
grant usage on all schemas in database raw to role transformer;grant select on all tables in database raw to role transformer;grant select on all views in database raw to role transformer;
```

transformer also needs to be able to create in the analytics database:
```
grant all on database analytics to role transformer;
```

  1. Let reporter read the transformed data


A previous version of this article recommended this be implemented through hooks in dbt, but this way lets you get away with a one-off statement.
```
grant usage on database analytics to role reporter;grant usage on future schemas in database analytics to role reporter;grant select on future tables in database analytics to role reporter;grant select on future views in database analytics to role reporter;
```

Again, if you already have data in your analytics database, make sure you run:
```
grant usage on all schemas in database analytics to role reporter;grant select on all tables in database analytics to role reporter;grant select on all views in database analytics to role reporter;
```

  1. Maintain


When new users are added, make sure you add them to the right role! Everything else should be inherited automatically thanks to those `future` grants.
For more discussion and legacy information, refer to [this Discourse article](https://discourse.getdbt.com/t/setting-up-snowflake-the-exact-grant-statements-we-run/439).
## Example Snowflake permissions[​](https://docs.getdbt.com/reference/database-permissions/snowflake-permissions#example-snowflake-permissions "Direct link to Example Snowflake permissions")
The following example provides you with the SQL statements you can use to manage permissions.
**Note** that `warehouse_name`, `database_name`, and `role_name` are placeholders and you can replace them as needed for your organization's naming convention.
```
grant all on warehouse warehouse_name to role role_name;grant usage on database database_name to role role_name;grant create schema on database database_name to role role_name; grant usage on schema database.an_existing_schema to role role_name;grant create table on schema database.an_existing_schema to role role_name;grant create view on schema database.an_existing_schema to role role_name;grant usage on future schemas in database database_name to role role_name;grant monitor on future schemas in database database_name to role role_name;grant select on future tables in database database_name to role role_name;grant select on future views in database database_name to role role_name;grant usage on all schemas in database database_name to role role_name;grant monitor on all schemas in database database_name to role role_name;grant select on all tables in database database_name to role role_name;grant select on all views in database database_name to role role_name;
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/analysis-properties ---

[Skip to main content](https://docs.getdbt.com/reference/analysis-properties#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fanalysis-properties+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fanalysis-properties+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fanalysis-properties+so+I+can+ask+questions+about+it.)
We recommend you define analysis properties in your `analyses/` directory, which is illustrated in the [`analysis-paths`](https://docs.getdbt.com/reference/project-configs/analysis-paths) configuration. Analysis properties are "special properties" in that you can't configure them in the `dbt_project.yml` file or using `config()` blocks. Refer to [ Configs and properties](https://docs.getdbt.com/reference/define-properties#which-properties-are-not-also-configs) for more info.
You can name these files `whatever_you_want.yml`, and nest them arbitrarily deeply in subfolders within the `analyses/` or `models/` directory.
analyses/<filename>.yml
```
analyses:-name: <analysis_name# required: <markdown_string>config:: # changed to config in v1.10show: true | falsenode_color: <color_id# Use name (such as node_color: purple) or hex code with quotes (such as node_color: "#cd7f32"): <string> | [<string>]columns:-name: <column_name: <markdown_string>-name:...# declare properties of additional columns-name:...# declare properties of additional analyses
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0


--- SOURCE: https://docs.getdbt.com/reference/artifacts/sources-json ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/sources-json#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fsources-json+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fsources-json+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fsources-json+so+I+can+ask+questions+about+it.)
On this page
**Current schema:**
**Produced by:** [`source freshness`](https://docs.getdbt.com/reference/commands/source)
This file contains information about [sources with freshness checks](https://docs.getdbt.com/docs/build/sources#checking-source-freshness). Today, dbt uses this file to power its [Source Freshness visualization](https://docs.getdbt.com/docs/build/sources#source-data-freshness).
### Top-level keys[​](https://docs.getdbt.com/reference/artifacts/sources-json#top-level-keys "Direct link to Top-level keys")
  * `elapsed_time`: Total invocation time in seconds.
  * `results`: Array of freshness-check execution details.


Each entry in `results` is a dictionary with the following keys:
  * `unique_id`: Unique source node identifier, which map results to `sources` in the [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json)
  * `max_loaded_at`: Max value of `loaded_at_field` timestamp in the source table when queried.
  * `snapshotted_at`: Current timestamp when querying.
  * `max_loaded_at_time_ago_in_s`: Interval between `max_loaded_at` and `snapshotted_at`, calculated in python to handle timezone complexity.
  * `criteria`: The freshness threshold(s) for this source, defined in the project.
  * `status`: The freshness status of this source, based on `max_loaded_at_time_ago_in_s` + `criteria`, reported on the CLI. One of `pass`, `warn`, or `error` if the query succeeds, `runtime error` if the query fails.
  * `execution_time`: Total time spent checking freshness for this source
  * `timing`: Array that breaks down execution time into steps (`compile` + `execute`)


  * `adapter_response`: Dictionary of metadata returned from the database, which varies by adapter. For example, success `code`, number of `rows_affected`, total `bytes_processed`, and so on. Not applicable for [data tests](https://docs.getdbt.com/docs/build/data-tests).
    * `rows_affected` returns the number of rows modified by the last statement executed. In cases where the query's row count can't be determined or isn't applicable (such as when creating a view), a [standard value](https://peps.python.org/pep-0249/#rowcount) of `-1` is returned for `rowcount`.


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/build ---

[Skip to main content](https://docs.getdbt.com/reference/commands/build#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fbuild+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fbuild+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fbuild+so+I+can+ask+questions+about+it.)
On this page
The `dbt build` command will:
  * test [tests](https://docs.getdbt.com/docs/build/data-tests)
  * snapshot [snapshots](https://docs.getdbt.com/docs/build/snapshots)
  * seed [seeds](https://docs.getdbt.com/docs/build/seeds)
  * build [user-defined functions](https://docs.getdbt.com/docs/build/udfs) (available from dbt Core v1.11 and in the dbt Fusion engine)


In DAG order, for selected resources or an entire project.
## Details[​](https://docs.getdbt.com/reference/commands/build#details "Direct link to Details")
**Artifacts:** The `build` task will write a single [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json) and a single [run results artifact](https://docs.getdbt.com/reference/artifacts/run-results-json). The run results will include information about all models, tests, seeds, and snapshots that were selected to build, combined into one file.
**Skipping on failures:** Tests on upstream resources will block downstream resources from running, and a test failure will cause those downstream resources to skip entirely. E.g. If `model_b` depends on `model_a`, and a `unique` test on `model_a` fails, then `model_b` will `SKIP`.
  * Don't want a test to cause skipping? Adjust its [severity or thresholds](https://docs.getdbt.com/reference/resource-configs/severity) to `warn` instead of `error`
  * In the case of a test with multiple parents, where one parent depends on the other (e.g. a `relationships` test between `model_a` + `model_b`), that test will block-and-skip children of the most-downstream parent only (`model_b`).
  * If you have a test with multiple parents that are independent of each other, dbt [skips](https://github.com/dbt-labs/dbt-core/blob/d5071fa13502be273596a0b7c8b13d14b6c68655/core/dbt/compilation.py#L224-L257) the downstream node only if that node depends on all of those parents.


**Selecting resources:** The `build` task supports standard selection syntax (`--select`, `--exclude`, `--selector`), as well as a `--resource-type` flag that offers a final filter (just like `list`). Whichever resources are selected, those are the ones that `build` will run/test/snapshot/seed.
  * Remember that tests support indirect selection, so `dbt build -s model_a` will both run _and_ test `model_a`. What does that mean? Any tests that directly depend on `model_a` will be included, so long as those tests don't also depend on other unselected parents. See [test selection](https://docs.getdbt.com/reference/node-selection/test-selection-examples) for details and examples.


**Flags:** The `build` task supports all the same flags as `run`, `test`, `snapshot`, and `seed`. For flags that are shared between multiple tasks (e.g. `--full-refresh`), `build` will use the same value for all selected resource types (e.g. both models and seeds will be full refreshed).
### The `--empty` flag[​](https://docs.getdbt.com/reference/commands/build#the---empty-flag "Direct link to the---empty-flag")
The `build` command supports the `--empty` flag for building schema-only dry runs. The `--empty` flag limits the refs and sources to zero rows. dbt will still execute the model SQL against the target data warehouse but will avoid expensive reads of input data. This validates dependencies and ensures your models will build properly.
#### The render method[​](https://docs.getdbt.com/reference/commands/build#the-render-method "Direct link to The render method")
The `.render()` method is generally used to resolve or evaluate Jinja expressions (such as `{{ source(...) }}`) during runtime.
When using the `--empty flag`, dbt may skip processing `ref()` or `source()` for optimization. To avoid compilation errors and to explicitly tell dbt to process a specific relation (`ref()` or `source()`), use the `.render()` method in your model file. For example:
models.sql
```
{{ config(    pre_hook = [        "alter external table {{ source('sys', 'customers').render() }} refresh") }}select ...
```

## Tests[​](https://docs.getdbt.com/reference/commands/build#tests "Direct link to Tests")
When `dbt build` is executed with unit tests applied, the models will be processed according to their lineage and dependencies. The tests will be executed as follows:
  * [Unit tests](https://docs.getdbt.com/docs/build/unit-tests) are run on a SQL model.
  * The model is materialized.
  * [Data tests](https://docs.getdbt.com/docs/build/data-tests) are run on the model.


This saves on warehouse spend as the model will only be materialized if the unit tests pass successfully.
Unit tests and data tests can be selected using `--select test_type:unit` or `--select test_type:data` for `dbt build` (same for the `--exclude` flag).
### Examples[​](https://docs.getdbt.com/reference/commands/build#examples "Direct link to Examples")
```
$ dbt buildRunning with dbt=1.9.0-b2Found 1 model, 4 tests, 1 snapshot, 1 analysis, 341 macros, 0 operations, 1 seed file, 2 sources, 2 exposures18:49:43 | Concurrency: 1 threads (target='dev')18:49:43 |18:49:43 | 1 of 7 START seed file dbt_jcohen.my_seed............................ [RUN]18:49:43 | 1 of 7 OK loaded seed file dbt_jcohen.my_seed........................ [INSERT 2 in 0.09s]18:49:43 | 2 of 7 START view model dbt_jcohen.my_model.......................... [RUN]18:49:43 | 2 of 7 OK created view model dbt_jcohen.my_model..................... [CREATE VIEW in 0.12s]18:49:43 | 3 of 7 START test not_null_my_seed_id................................ [RUN]18:49:43 | 3 of 7 PASS not_null_my_seed_id...................................... [PASS in 0.05s]18:49:43 | 4 of 7 START test unique_my_seed_id.................................. [RUN]18:49:43 | 4 of 7 PASS unique_my_seed_id........................................ [PASS in 0.03s]18:49:43 | 5 of 7 START snapshot snapshots.my_snapshot.......................... [RUN]18:49:43 | 5 of 7 OK snapshotted snapshots.my_snapshot.......................... [INSERT 0 5 in 0.27s]18:49:43 | 6 of 7 START test not_null_my_model_id............................... [RUN]18:49:43 | 6 of 7 PASS not_null_my_model_id..................................... [PASS in 0.03s]18:49:43 | 7 of 7 START test unique_my_model_id................................. [RUN]18:49:43 | 7 of 7 PASS unique_my_model_id....................................... [PASS in 0.02s]18:49:43 |18:49:43 | Finished running 1 seed, 1 view model, 4 tests, 1 snapshot in 1.01s.Completed successfullyDone. PASS=7 WARN=0 ERROR=0 SKIP=0 TOTAL=7
```

## Functions[​](https://docs.getdbt.com/reference/commands/build#functions "Direct link to Functions")
_Available from dbt Core v1.11 and in the dbt Fusion engine_
The `build` command builds [user-defined functions](https://docs.getdbt.com/docs/build/udfs) as part of the DAG execution. To build or rebuild only `functions` in your project, run `dbt build --select "resource_type:function"`. For example:
```
dbt build --select"resource_type:function"dbt-fusion 2.0.0-preview.45 Succeeded [0.98s]function dbt_schema.whoami (function) Succeeded [1.12s]function dbt_schema.area_of_circle (function)
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/cmd-docs ---

[Skip to main content](https://docs.getdbt.com/reference/commands/cmd-docs#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fcmd-docs+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fcmd-docs+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fcmd-docs+so+I+can+ask+questions+about+it.)
On this page
`dbt docs` has two supported subcommands: `generate` and `serve`.
### dbt docs generate[​](https://docs.getdbt.com/reference/commands/cmd-docs#dbt-docs-generate "Direct link to dbt docs generate")
The command is responsible for generating your project's documentation website by
  1. Copying the website `index.html` file into the `target/` directory.
  2. Compiling the resources in your project, so that their `compiled_code` will be included in [`manifest.json`](https://docs.getdbt.com/reference/artifacts/manifest-json).
  3. Running queries against database metadata to produce the [`catalog.json`](https://docs.getdbt.com/reference/artifacts/catalog-json) file, which contains metadata about the tables and views produced by the models in your project.


**Example** :
```
dbt docs generate
```

Use the `--select` argument to limit the nodes included within `catalog.json`. When this flag is provided, step (3) will be restricted to the selected nodes. All other nodes will be excluded. Step (2) is unaffected.
**Example** :
```
dbt docs generate --select +orders
```

Use the `--no-compile` argument to skip re-compilation. When this flag is provided, `dbt docs generate` will skip step (2) described above. Note that dbt still runs certain special macros (like `generate_schema_name`) [during parsing](https://docs.getdbt.com/reference/global-configs/parsing), even when compilation is skipped.
**Example** :
```
dbt docs generate --no-compile
```

Use the `--empty-catalog` argument to skip running the database queries to populate `catalog.json`. When this flag is provided, `dbt docs generate` will skip step (3) described above.
This is not recommended for production environments, as it means that your documentation will be missing information gleaned from database metadata (the full set of columns in each table, and statistics about those tables). It can speed up `docs generate` in development, when you just want to visualize lineage and other information defined within your project. To learn how to build your documentation in dbt, refer to [build your docs in dbt](https://docs.getdbt.com/docs/explore/build-and-view-your-docs).
**Example** :
```
dbt docs generate --empty-catalog
```

**Example** :
Use the `--static` flag to generate the docs as a static page for hosting on a cloud storage provider. The `catalog.json` and `manifest.json` files will be inserted into the `index.html` file, creating a single page easily shared via email or file-sharing apps.
```
dbt docs generate --static
```

### dbt docs serve[​](https://docs.getdbt.com/reference/commands/cmd-docs#dbt-docs-serve "Direct link to dbt docs serve")
This command starts a webserver on port 8080 to serve your documentation locally and opens the documentation site in your default browser. The webserver is rooted in your `target/` directory. Be sure to run `dbt docs generate` before `dbt docs serve` because the `generate` command produces a [catalog metadata artifact](https://docs.getdbt.com/reference/artifacts/catalog-json) that the `serve` command depends upon. You will see an error message if the catalog is missing.
Use the `dbt docs serve` command if you're developing locally with the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation) or [dbt Core](https://docs.getdbt.com/docs/local/install-dbt). The [Studio IDE](https://docs.getdbt.com/docs/cloud/studio-ide/develop-in-studio) doesn't support this command.
**Usage:**
You may specify a different port using the `--port` flag.
**Example** :
```
dbt docs serve --port 8001
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/sl-manifest ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/sl-manifest#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fsl-manifest+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fsl-manifest+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fsl-manifest+so+I+can+ask+questions+about+it.)
On this page
**Produced by:** Any command that parses your project. This includes all commands _except_ [`deps`](https://docs.getdbt.com/reference/commands/deps), [`clean`](https://docs.getdbt.com/reference/commands/clean), [`debug`](https://docs.getdbt.com/reference/commands/debug), and [`init`](https://docs.getdbt.com/reference/commands/init).
dbt creates an [artifact](https://docs.getdbt.com/reference/artifacts/dbt-artifacts) file called the _Semantic Manifest_ (`semantic_manifest.json`), which MetricFlow requires to build and run metric queries properly for the dbt Semantic Layer. This artifact contains comprehensive information about your dbt Semantic Layer. It is an internal file that acts as the integration point with MetricFlow.
By using the semantic manifest produced by dbt Core, MetricFlow will instantiate a data flow plan and generate SQL from Semantic Layer query requests. It's a valuable reference that you can use to understand the structure and details of your data models.
Similar to the [`manifest.json` file](https://docs.getdbt.com/reference/artifacts/manifest-json), the `semantic_manifest.json` file also lives in the [target directory](https://docs.getdbt.com/reference/global-configs/json-artifacts) of your dbt project where dbt stores various artifacts (such as compiled models and tests) generated during the execution of your project.
There are two reasons why `semantic_manifest.json` exists alongside `manifest.json`:
  * Deserialization: `dbt-core` and MetricFlow use different libraries for handling data serialization.
  * Efficiency and performance: MetricFlow and the dbt Semantic Layer need specific semantic details from the manifest. By trimming down the information printed into `semantic_manifest.json`, the process becomes more efficient and enables faster data handling between `dbt-core` and MetricFlow.


## Top-level keys[​](https://docs.getdbt.com/reference/artifacts/sl-manifest#top-level-keys "Direct link to Top-level keys")
### Example[​](https://docs.getdbt.com/reference/artifacts/sl-manifest#example "Direct link to Example")
target/semantic_manifest.json
```
"semantic_models":["name":"semantic model name","defaults":null,"description":"semantic model description","node_relation":{"alias":"model alias","schema_name":"model schema","database":"model db","relation_name":"Fully qualified relation name""entities":["entities in the semantic model"],"measures":["measures in the semantic model"],"dimensions":["dimensions in the semantic model"],"metrics":["name":"name of the metric","description":"metric description","type":"metric type","type_params":{"measure":{"name":"name for measure","filter":"filter for measure","alias":"alias for measure""numerator":null,"denominator":null,"expr":null,"window":null,"grain_to_date":null,"metrics":["metrics used in defining the metric. this is used in derived metrics"],"input_measures":[]"filter":null,"metadata":null"project_configuration":{"time_spine_table_configurations":["location":"fully qualified table name for timespine","column_name":"date column","grain":"day""metadata":null,"dsi_package_version":{}"saved_queries":["name":"name of the saved query","query_params":{"metrics":["metrics used in the saved query""group_by":["TimeDimension('model_primary_key__date_column', 'day')","Dimension('model_primary_key__metric_one')","Dimension('model__dimension')""where":null"description":"Description of the saved query","metadata":null,"label":null,"exports":["name":"saved_query_name","config":{"export_as":"view","schema_name":null,"alias":null
```

## Related docs[​](https://docs.getdbt.com/reference/artifacts/sl-manifest#related-docs "Direct link to Related docs")
  * [Semantic Layer API](https://docs.getdbt.com/docs/dbt-cloud-apis/sl-api-overview)
  * [About dbt artifacts](https://docs.getdbt.com/reference/artifacts/dbt-artifacts)


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/run-results-json ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/run-results-json#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Frun-results-json+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Frun-results-json+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Frun-results-json+so+I+can+ask+questions+about+it.)
On this page
**Current schema** :
**Produced by:** [`build`](https://docs.getdbt.com/reference/commands/build) [`clone`](https://docs.getdbt.com/reference/commands/clone) [`compile`](https://docs.getdbt.com/reference/commands/compile) [`docs generate`](https://docs.getdbt.com/reference/commands/cmd-docs) [`retry`](https://docs.getdbt.com/reference/commands/retry) [`run`](https://docs.getdbt.com/reference/commands/run) [`seed`](https://docs.getdbt.com/reference/commands/seed) [`show`](https://docs.getdbt.com/reference/commands/show) [`snapshot`](https://docs.getdbt.com/reference/commands/snapshot) [`test`](https://docs.getdbt.com/reference/commands/test) [`run-operation`](https://docs.getdbt.com/reference/commands/run-operation)
This file contains information about a completed invocation of dbt, including timing and status info for each node (model, test, etc) that was executed. In aggregate, many `run_results.json` can be combined to calculate average model runtime, test failure rates, the number of record changes captured by snapshots, etc.
Note that only executed nodes appear in the run results. If you have multiple run or test steps with different critiera, each will produce different run results.
Note: `dbt source freshness` produces a different artifact, [`sources.json`](https://docs.getdbt.com/reference/artifacts/sources-json), with similar attributes.
### Top-level keys[​](https://docs.getdbt.com/reference/artifacts/run-results-json#top-level-keys "Direct link to Top-level keys")
  * `args`: Dictionary of arguments passed to the CLI command or RPC method that produced this artifact. Most useful is `which` (command) or `rpc_method`. This dict excludes null values, and includes default values if they are not null. Equivalent to [`invocation_args_dict`](https://docs.getdbt.com/reference/dbt-jinja-functions/flags#invocation_args_dict) in the dbt-Jinja context.
  * `elapsed_time`: Total invocation time in seconds.
  * `results`: Array of node execution details.


Each entry in `results` is a [`Result` object](https://docs.getdbt.com/reference/dbt-classes#result-objects), with one difference: Instead of including the entire `node` object, only the `unique_id` is included. (The full `node` object is recorded in [`manifest.json`](https://docs.getdbt.com/reference/artifacts/manifest-json).)
  * `unique_id`: Unique node identifier, which maps results to `nodes` in the [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json)
  * `status`: dbt's interpretation of runtime success, failure, or error
  * `thread_id`: Which thread executed this node? E.g. `Thread-1`
  * `execution_time`: Total time spent executing this node
  * `timing`: Array that breaks down execution time into steps (often `compile` + `execute`)
  * `message`: How dbt will report this result on the CLI, based on information returned from the database


  * `adapter_response`: Dictionary of metadata returned from the database, which varies by adapter. For example, success `code`, number of `rows_affected`, total `bytes_processed`, and so on. Not applicable for [data tests](https://docs.getdbt.com/docs/build/data-tests).
    * `rows_affected` returns the number of rows modified by the last statement executed. In cases where the query's row count can't be determined or isn't applicable (such as when creating a view), a [standard value](https://peps.python.org/pep-0249/#rowcount) of `-1` is returned for `rowcount`.


The run_results.json includes three attributes related to the `applied` state that complement `unique_id`:
  * `compiled`: Boolean entry of the node compilation status (`False` after parsing, but `True` after compiling).
  * `compiled_code`: Rendered string of the code that was compiled (empty after parsing, but full string after compiling).
  * `relation_name`: The fully-qualified name of the object that was (or will be) created/updated within the database.


Continue to look up additional information about the `logical` state of nodes using the full node object in manifest.json via the `unique_id`.
## Examples[​](https://docs.getdbt.com/reference/artifacts/run-results-json#examples "Direct link to Examples")
Here are a few examples and the resulting output to the `run_results.json` file.
### Compile model results[​](https://docs.getdbt.com/reference/artifacts/run-results-json#compile-model-results "Direct link to Compile model results")
Let's say that you have a model that looks like this:
models/my_model.sql
```
select {{ dbt.current_timestamp() }} as created_at
```

Compile the model:
```
dbt compile -s my_model
```

Here's a printed snippet from the `run_results.json`:
```
"status":"success","timing":["name":"compile","started_at":"2023-10-12T16:35:28.510434Z","completed_at":"2023-10-12T16:35:28.519086Z""name":"execute","started_at":"2023-10-12T16:35:28.521633Z","completed_at":"2023-10-12T16:35:28.521641Z""thread_id":"Thread-2","execution_time":0.0408780574798584,"adapter_response":{},"message":null,"failures":null,"unique_id":"model.my_project.my_model","compiled":true,"compiled_code":"select now() as created_at","relation_name":"\"postgres\".\"dbt_dbeatty\".\"my_model\""
```

### Run generic data tests[​](https://docs.getdbt.com/reference/artifacts/run-results-json#run-generic-data-tests "Direct link to Run generic data tests")
Use the [`store_failures_as`](https://docs.getdbt.com/reference/resource-configs/store_failures_as) config to store failures for only one data test in the database:
models/_models.yml
```
models:-name: my_modelcolumns:-name: created_atdata_tests:-not_null:config:store_failures_as: view-unique:config:store_failures_as: ephemeral
```

Run the built-in `unique` test and store the failures as a table:
```
dbt test-s my_model
```

Here's a printed snippet from the `run_results.json`:
```
"results":["status":"pass","timing":["name":"compile","started_at":"2023-10-12T17:20:51.279437Z","completed_at":"2023-10-12T17:20:51.317312Z""name":"execute","started_at":"2023-10-12T17:20:51.319812Z","completed_at":"2023-10-12T17:20:51.441967Z""thread_id":"Thread-2","execution_time":0.1807551383972168,"adapter_response":{"_message":"SELECT 1","code":"SELECT","rows_affected":1"message":null,"failures":0,"unique_id":"test.my_project.unique_my_model_created_at.a9276afbbb","compiled":true,"compiled_code":"\n    \n    \n\nselect\n    created_at as unique_field,\n    count(*) as n_records\n\nfrom \"postgres\".\"dbt_dbeatty\".\"my_model\"\nwhere created_at is not null\ngroup by created_at\nhaving count(*) > 1\n\n\n","relation_name":null"status":"pass","timing":["name":"compile","started_at":"2023-10-12T17:20:51.274049Z","completed_at":"2023-10-12T17:20:51.295237Z""name":"execute","started_at":"2023-10-12T17:20:51.296361Z","completed_at":"2023-10-12T17:20:51.491327Z""thread_id":"Thread-1","execution_time":0.22345590591430664,"adapter_response":{"_message":"SELECT 1","code":"SELECT","rows_affected":1"message":null,"failures":0,"unique_id":"test.my_project.not_null_my_model_created_at.9b412fbcc7","compiled":true,"compiled_code":"\n    \n    \n\n\n\nselect *\nfrom \"postgres\".\"dbt_dbeatty\".\"my_model\"\nwhere created_at is null\n\n\n","relation_name":"\"postgres\".\"dbt_dbeatty_dbt_test__audit\".\"not_null_my_model_created_at\""
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/clean ---

[Skip to main content](https://docs.getdbt.com/reference/commands/clean#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fclean+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fclean+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fclean+so+I+can+ask+questions+about+it.)
On this page
`dbt clean` is a utility function that deletes the paths specified within the [`clean-targets`](https://docs.getdbt.com/reference/project-configs/clean-targets) list in the `dbt_project.yml` file. It helps by removing unnecessary files or directories generated during the execution of other dbt commands, ensuring a clean state for the project.
## Example usage[​](https://docs.getdbt.com/reference/commands/clean#example-usage "Direct link to Example usage")
```
dbt clean
```

## Supported flags[​](https://docs.getdbt.com/reference/commands/clean#supported-flags "Direct link to Supported flags")
This section will briefly explain the following flags:
  * [`--clean-project-files-only`](https://docs.getdbt.com/reference/commands/clean#--clean-project-files-only) (default)
  * [`--no-clean-project-files-only`](https://docs.getdbt.com/reference/commands/clean#--no-clean-project-files-only)


To view the list of all supported flags for the `dbt clean` command in the terminal, use the `--help` flag, which will display detailed information about the available flags you can use, including its description and usage:
```
dbt clean --help
```

### --clean-project-files-only[​](https://docs.getdbt.com/reference/commands/clean#--clean-project-files-only "Direct link to --clean-project-files-only")
By default, dbt deletes all the paths within the project directory specified in `clean-targets`.
Avoid using paths outside the dbt project; otherwise, you will see an error.
#### Example usage[​](https://docs.getdbt.com/reference/commands/clean#example-usage-1 "Direct link to Example usage")
```
dbt clean --clean-project-files-only
```

### --no-clean-project-files-only[​](https://docs.getdbt.com/reference/commands/clean#--no-clean-project-files-only "Direct link to --no-clean-project-files-only")
Deletes all the paths specified in the `clean-targets` list of `dbt_project.yml`, including those outside the current dbt project.
```
dbt clean --no-clean-project-files-only
```

## dbt clean with remote file system[​](https://docs.getdbt.com/reference/commands/clean#dbt-clean-with-remote-file-system "Direct link to dbt clean with remote file system")
To avoid complex permissions issues and potentially deleting crucial aspects of the remote file system without access to fix them, this command does not work when interfacing with the RPC server that powers the Studio IDE. Instead, when working in dbt, the `dbt deps` command cleans before it installs packages automatically. The `target` folder can be manually deleted from the sidebar file tree if needed.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/init ---

[Skip to main content](https://docs.getdbt.com/reference/commands/init#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Finit+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Finit+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Finit+so+I+can+ask+questions+about+it.)
On this page
`dbt init` helps get you started using dbt Core!
## New project[​](https://docs.getdbt.com/reference/commands/init#new-project "Direct link to New project")
If this is your first time ever using the tool, it will:
  * ask you to name your project
  * ask you which database adapter you're using (or to [Supported Data Platforms](https://docs.getdbt.com/docs/supported-data-platforms))
  * prompt you for each piece of information that dbt needs to connect to that database: things like `account`, `user`, `password`, etc


Then, it will:
  * Create a new folder with your project name and sample files, enough to get you started with dbt
  * Create a connection profile on your local machine. The default location is `~/.dbt/profiles.yml`. Read more in [configuring your profile](https://docs.getdbt.com/docs/local/profiles.yml).


When using `dbt init` to initialize your project, include the `--profile` flag to specify an existing `profiles.yml` as the `profile:` key to use instead of creating a new one. For example, `dbt init --profile profile_name`.
If the profile does not exist in `profiles.yml` or the command is run inside an existing project, the command raises an error.
## Existing project[​](https://docs.getdbt.com/reference/commands/init#existing-project "Direct link to Existing project")
If you've just cloned or downloaded an existing dbt project, `dbt init` can still help you set up your connection profile so that you can start working quickly. It will prompt you for connection information, as above, and add a profile (using the `profile` name from the project) to your local `profiles.yml`, or create the file if it doesn't already exist.
## profile_template.yml[​](https://docs.getdbt.com/reference/commands/init#profile_templateyml "Direct link to profile_template.yml")
`dbt init` knows how to prompt for connection information by looking for a file named `profile_template.yml`. It will look for this file in two places:
  * **Adapter plugin:** What's the bare minimum Postgres profile? What's the type of each field, what are its defaults? This information is stored in a file called [`dbt/include/postgres/profile_template.yml`](https://github.com/dbt-labs/dbt-postgres/blob/main/dbt/include/postgres/profile_template.yml). If you're the maintainer of an adapter plugin, we highly recommend that you add a `profile_template.yml` to your plugin, too. Refer to the [Build, test, document, and promote adapters](https://docs.getdbt.com/guides/adapter-creation) guide for more information.
  * **Existing project:** If you're the maintainer of an existing project, and you want to help new users get connected to your database quickly and easily, you can include your own custom `profile_template.yml` in the root of your project, alongside `dbt_project.yml`. For common connection attributes, set the values in `fixed`; leave user-specific attributes in `prompts`, but with custom hints and defaults as you'd like.


profile_template.yml
```
fixed:account: abc123authenticator: externalbrowserdatabase: analyticsrole: transformertype: snowflakewarehouse: transformingprompts:target:type: stringhint: your desired target nametype: stringhint: yourname@jaffleshop.comschema:type: stringhint: usually dbt_<yournamethreads:hint:"your favorite number, 1-10"type: intdefault:8
```

```
$ dbt initRunning with dbt=1.0.0Setting up your profile.user (yourname@jaffleshop.com): summerintern@jaffleshop.comschema (usually dbt_<yourname>): dbt_summerinternthreads (your favorite number, 1-10) [8]: 6Profile internal-snowflake written to /Users/intern/.dbt/profiles.yml using project's profile_template.yml and your supplied values. Run 'dbt debug' to validate the connection.
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/other-artifacts ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fother-artifacts+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fother-artifacts+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fother-artifacts+so+I+can+ask+questions+about+it.)
On this page
### index.html[​](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#indexhtml "Direct link to index.html")
**Produced by:** [`docs generate`](https://docs.getdbt.com/reference/commands/cmd-docs)
This file is the skeleton of the [auto-generated dbt documentation website](https://docs.getdbt.com/docs/explore/build-and-view-your-docs). The contents of the site are populated by the [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json) and [catalog](https://docs.getdbt.com/reference/artifacts/catalog-json).
Note: the source code for `index.json` comes from the [dbt-docs repo](https://github.com/dbt-labs/dbt-docs). Head over there if you want to make a bug report, suggestion, or contribution relating to the documentation site.
### partial_parse.msgpack[​](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#partial_parsemsgpack "Direct link to partial_parse.msgpack")
**Produced by:** [manifest commands](https://docs.getdbt.com/reference/artifacts/manifest-json) + [`parse`](https://docs.getdbt.com/reference/commands/parse)
This file is used to store a compressed representation of files dbt has parsed. If you have [partial parsing](https://docs.getdbt.com/reference/parsing#partial-parsing) enabled, dbt will use this file to identify the files that have changed and avoid re-parsing the rest.
### graph.gpickle[​](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#graphgpickle "Direct link to graph.gpickle")
**Produced by:** commands supporting [node selection](https://docs.getdbt.com/reference/node-selection/syntax)
Stores the network representation of the dbt resource DAG.
### graph_summary.json[​](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#graph_summaryjson "Direct link to graph_summary.json")
**Produced by:** [manifest commands](https://docs.getdbt.com/reference/artifacts/manifest-json)
This file is useful for investigating performance issues in dbt Core's graph algorithms.
It is more anonymized and compact than [`manifest.json`](https://docs.getdbt.com/reference/artifacts/manifest-json) and [`graph.gpickle`](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#graph.gpickle).
It includes that information at two separate points in time:
  1. `linked` — immediately after the graph is linked together, and
  2. `with_test_edges` — after test edges have been added.


Each of those points in time contains the `name` and `type` of each node and `succ` contains the keys of its child nodes.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Was this page helpful?](https://docs.getdbt.com/reference/artifacts/other-artifacts?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/dbt-environment ---

[Skip to main content](https://docs.getdbt.com/reference/commands/dbt-environment#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdbt-environment+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdbt-environment+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdbt-environment+so+I+can+ask+questions+about+it.)
On this page
The dbt platform CLI provides the `dbt environment` command for environment and connection details. If you're using Fusion or dbt Core, use `dbt debug` to inspect profile, target, and connection — or use `dbtf debug` if you have more than one dbt CLI and want to inspect Fusion.
The `dbt environment` command enables you to interact with your dbt environment. Use the command for:
  * Viewing your local configuration details (account ID, active project ID, deployment environment, and more).
  * Viewing your dbt configuration details (environment ID, environment name, connection type, and more).


This guide lists all the commands and options you can use with `dbt environment` in the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation). To use them, add a command or option like this: `dbt environment [command]` or use the shorthand `dbt env [command]`.
### dbt environment show[​](https://docs.getdbt.com/reference/commands/dbt-environment#dbt-environment-show "Direct link to dbt environment show")
The `show` command allows you to view your local and dbt configuration details. To run the command with the dbt CLI, enter one of the following commands, including the shorthand:
```
dbt environment show
```

```
dbt env show
```

The command returns the following information:
```
❯ dbt env showLocal Configuration:  Active account ID              185854  Active project ID              271692  Active host name               cloud.getdbt.com  dbt_cloud.yml file path        /Users/cesar/.dbt/dbt_cloud.yml  dbt_project.yml file path      /Users/cesar/git/cloud-cli-test-project/dbt_project.ymlConstant name="cloud" / CLI version          0.35.7  OS info                        darwin arm64Cloud Configuration:  Account ID                     185854  Project ID                     271692  Project name                   Snowflake  Environment ID                 243762  Environment name               Development  Defer environment ID           [N/A]  dbt version                    1.6.0-latest  Target name                    default  Connection type                snowflakeSnowflake Connection Details:  Account                        ska67070  Warehouse                      DBT_TESTING_ALT  Database                       DBT_TEST  Schema                         CLOUD_CLI_TESTING  Role                           SYSADMIN  User                           dbt_cloud_user  Client session keep alive      false
```

Note, that dbt won't return anything that is a secret key and will return an 'NA' for any field that isn't configured.
### dbt environment flags[​](https://docs.getdbt.com/reference/commands/dbt-environment#dbt-environment-flags "Direct link to dbt environment flags")
Use the following flags (or options) with the `dbt environment` command:
  * `-h`, `--help` — To view the help documentation for a specific command in your command line interface.
```
dbt environment [command]--help
```

The `--help` flag returns the following information:
```
  ❯ dbt help environment  Interact with dbt environmentsUsage:  dbt environment [command]Aliases:  environment, envAvailable Commands:  show        Show the working environmentFlags:  -h, --helphelpfor environmentUse "dbt environment [command] --help"formore information about a command.
```

For example, to view the help documentation for the `show` command, enter one of the following commands, including the shorthand:
```
dbt environment show --helpdbt env show -h
```



## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/debug ---

[Skip to main content](https://docs.getdbt.com/reference/commands/debug#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdebug+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdebug+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdebug+so+I+can+ask+questions+about+it.)
On this page
Use dbt debug to test database connections and check system setup.
`dbt debug` is a utility function to test the database connection and display information for debugging purposes, such as the validity of your project file, the [dbt version](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt_version), and your installation of any requisite dependencies (like `git` when you run `dbt deps`).
It checks your database connection, local configuration, and system setup across multiple axes to help identify potential issues before running dbt commands.
By default, `dbt debug` validates:
  * **Database connection** (for configured profiles)
  * **dbt project setup** (like `dbt_project.yml` validity)
  * **System environment** (OS, Python version, installed dbt version)
  * **Required dependencies** (such as `git` for `dbt deps`)
  * **Adapter details** (installed adapter versions and compatibility)


*Note: Not to be confused with [debug-level logging](https://docs.getdbt.com/reference/global-configs/logs#debug-level-logging) through the `--debug` option which increases verbosity.
## Flags[​](https://docs.getdbt.com/reference/commands/debug#flags "Direct link to Flags")
Most of the `dbt debug` flags apply to the dbt Core CLI. Some flags also work in dbt CLI, but only `--connection` is supported in the Studio IDE.
  * dbt Core CLI: Supports all flags.
  * Studio IDE: Only supports dbt `debug` and `dbt debug --connection`.
  * dbt CLI: Only supports dbt `debug` and `dbt debug --connection`. You can also use the [`dbt environment`](https://docs.getdbt.com/reference/commands/dbt-environment) command to interact with your dbt environment.


`dbt debug` supports the following flags in your terminal when using the command line interface (CLI):
```
Usage: dbt debug [OPTIONS] Show information on the current dbt environment and check dependencies, then test the database connection. Not to be confused with the --debug option which increases verbosity.Options: --cache-selected-only / --no-cache-selected-only                At start of run, populate relational cache                only for schemas containing selected nodes,                or for all schemas of interest. -d, --debug / --no-debug                    Display debug logging during dbt execution.                Useful for debugging and making bug reports. --defer / --no-defer                      If set, resolve unselected nodes by                deferring to the manifest within the --state                directory. --defer-state DIRECTORY                     Override the state directory for deferral                only. --deprecated-favor-state TEXT                  Internal flag for deprecating old env var. -x, --fail-fast / --no-fail-fast                 Stop execution on first failure. --favor-state / --no-favor-state                If set, defer to the argument provided to                the state flag for resolving unselected                nodes, even if the node(s) exist as a                database object in the current environment. --indirect-selection [eager|cautious|buildable|empty]                Controls which tests run based on their                relationships to selected models in your DAG.                Eager (default) is most inclusive and runs                tests that reference your selected models.                Cautious is most exclusive and only runs tests                that reference selected models.                Buildable is in between. Empty runs no tests. --log-cache-events / --no-log-cache-events                Enable verbose logging for relational cache                events to help when debugging. --log-format [text|debug|json|default]                Specify the format of logging to the console                and the log file. Use --log-format-file to                configure the format for the log file                differently than the console. --log-format-file [text|debug|json|default]                Specify the format of logging to the log                file by overriding the default value and the                general --log-format setting. --log-level [debug|info|warn|error|none]                Specify the minimum severity of events that                are logged to the console and the log file.                Use --log-level-file to configure the                severity for the log file differently than                the console. --log-level-file [debug|info|warn|error|none]                Specify the minimum severity of events that                are logged to the log file by overriding the                default value and the general --log-level                setting. --log-path PATH                         Configure the 'log-path'. Only applies this                setting for the current run. Overrides the                'DBT_LOG_PATH' if it is set. --partial-parse / --no-partial-parse                Allow for partial parsing by looking for and                writing to a pickle file in the target                directory. This overrides the user                configuration file. --populate-cache / --no-populate-cache                At start of run, use `show` or                `information_schema` queries to populate a                relational cache, which can speed up                subsequent materializations. --print / --no-print                      Output all {{ print() }} macro calls. --printer-width INTEGER                     Sets the width of terminal output --profile TEXT                         Which existing profile to load. Overrides                setting in dbt_project.yml. -q, --quiet / --no-quiet                    Suppress all non-error logging to stdout.                Does not affect {{ print() }} macro calls. -r, --record-timing-info PATH                  When this option is passed, dbt will output                low-level timing stats to the specified                file. Example: `--record-timing-info                output.profile` --send-anonymous-usage-stats / --no-send-anonymous-usage-stats                Send anonymous usage stats to dbt Labs. --state DIRECTORY                        Unless overridden, use this state directory                for both state comparison and deferral. --static-parser / --no-static-parser                Use the static parser. -t, --target TEXT                        Which target to load for the given profile --use-colors / --no-use-colors                 Specify whether log output is colorized in                the console and the log file. Use --use-                colors-file/--no-use-colors-file to colorize                the log file differently than the console. --use-colors-file / --no-use-colors-file                Specify whether log file output is colorized                by overriding the default value and the                general --use-colors/--no-use-colors                setting. --use-experimental-parser / --no-use-experimental-parser                Enable experimental parsing features. -V, -v, --version                        Show version information and exit --version-check / --no-version-check                If set, ensure the installed dbt version                matches the require-dbt-version specified in                the dbt_project.yml file (if any).                Otherwise, allow them to differ. --warn-error                   If dbt would normally warn, instead raise an                exception. Examples include --select that                selects nothing, deprecations,                configurations with no associated models,                invalid test configurations, and missing                sources/refs in tests. --warn-error-options WARNERROROPTIONSTYPE                If dbt would normally warn, instead raise an                exception based on include/exclude                configuration. Examples include --select                that selects nothing, deprecations,                configurations with no associated models,                invalid test configurations, and missing                sources/refs in tests. This argument should                be a YAML string, with keys 'include' or                'exclude'. eg. '{"include": "all",                "exclude": ["NoNodesForSelectionCriteria"]}' --write-json / --no-write-json                 Whether or not to write the manifest.json                and run_results.json files to the target                directory --connection                          Test the connection to the target database                independent of dependency checks.                Available in Studio IDE and dbt Core CLI --config-dir                          Print a system-specific command to access                the directory that the current dbt project                is searching for a profiles.yml. Then, exit.                This flag renders other debug step flags no- --profiles-dir PATH                       Which directory to look in for the                profiles.yml file. If not set, dbt will look                in the current working directory first, then                HOME/.dbt/ --project-dir PATH                       Which directory to look in for the                dbt_project.yml file. Default is the current                working directory and its parents. --vars YAML                           Supply variables to the project. This                argument overrides variables defined in your                dbt_project.yml file. This argument should                be a YAML string, eg. '{my_variable:                my_value}' -h, --help                           Show this message and exit.
```

## Example usage[​](https://docs.getdbt.com/reference/commands/debug#example-usage "Direct link to Example usage")
Only test the connection to the data platform and skip the other checks `dbt debug` looks for:
```
dbt debug --connection
```

Show the configured location for the `profiles.yml` file and exit:
```
dbt debug --config-dirTo view your profiles.yml file, run:open /Users/alice/.dbt
```

Test the connection in the Studio IDE:
```
dbt debug --connection
```

Test the connection in the Studio IDE
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/deps ---

[Skip to main content](https://docs.getdbt.com/reference/commands/deps?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdeps+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdeps+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fdeps+so+I+can+ask+questions+about+it.)
On this page
`dbt deps` pulls the most recent version of the dependencies listed in your `packages.yml` from git. See [Package-Management](https://docs.getdbt.com/docs/build/packages) for more information.
Where relevant, dbt will display up to date and/or latest versions of packages that are listed on dbt Hub. Example below.
> This does NOT apply to packages that are installed via git/local
```
packages:-package: dbt-labs/dbt_utilsversion: 0.7.1-package: brooklyn-data/dbt_artifactsversion: 1.2.0install-prerelease:true-package: dbt-labs/codegenversion: 0.4.0-package: calogica/dbt_expectationsversion: 0.4.1-git: https://github.com/dbt-labs/dbt_audit_helper.gitrevision: 0.4.0-git:"https://github.com/dbt-labs/dbt_labs-experimental-features"# git URLsubdirectory:"materialized-views"# name of subdirectory containing `dbt_project.yml`revision: 0.0.1-package: dbt-labs/snowplowversion: 0.13.0
```

```
Installing dbt-labs/dbt_utils@0.7.1  Installed from version 0.7.1  Up to date!Installing brooklyn-data/dbt_artifacts@1.2.0  Installed from version 1.2.0Installing dbt-labs/codegen@0.4.0  Installed from version 0.4.0  Up to date!Installing calogica/dbt_expectations@0.4.1  Installed from version 0.4.1  Up to date!Installing https://github.com/dbt-labs/dbt_audit_helper.git@0.4.0  Installed from revision 0.4.0Installing https://github.com/dbt-labs/dbt_labs-experimental-features@0.0.1  Installed from revision 0.0.1   and subdirectory materialized-viewsInstalling dbt-labs/snowplow@0.13.0  Installed from version 0.13.0  Updated version available: 0.13.1Installing calogica/dbt_date@0.4.0  Installed from version 0.4.0  Up to date!Updates available for packages: ['tailsdotcom/dbt_artifacts', 'dbt-labs/snowplow']Update your versions in packages.yml, then run dbt deps
```

## Predictable package installs[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#predictable-package-installs "Direct link to Predictable package installs")
dbt generates a `package-lock.yml` file in the root of your project. This file records the exact resolved versions (including commit SHAs) of all packages defined in your `packages.yml` or `dependencies.yml` file. The `package-lock.yml` file ensures consistent and repeatable installs across all environments.
When you run `dbt deps`, dbt installs packages based on the versions locked in the `package-lock.yml`. This means that as long as your packages file hasn’t changed, the exact same dependency versions will be installed even if newer versions of those packages have been released. This consistency is important to maintain stability in development and production environments, and to prevent unexpected issues from new releases with potential bugs.
If the `packages.yml` file has changed (for example, a new package is added or a version range is updated), then `dbt deps` automatically resolves the new set of dependencies and updates the lock file accordingly. You can also manually trigger an upgrade by running `dbt deps --upgrade`.
To maintain consistency, commit the `package-lock.yml` file to version control. This guarantees consistency across all environments and for all developers.
### Managing `package-lock.yml`[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#managing-package-lockyml "Direct link to managing-package-lockyml")
The `package-lock.yml` file should be committed to Git initially and updated only when you intend to change versions or uninstall a package. For example, run `dbt deps --upgrade` to get updated package versions or `dbt deps --lock` to update the lock file based on changes to the packages config without installing the packages.
To bypass using `package-lock.yml` entirely, you can add it to your project's `.gitignore`. However, this approach sacrifices the predictability of builds. If you choose this route, we strongly recommend adding version pins for third-party packages in your `packages` config.
### Detecting changes in `packages` config[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#detecting-changes-in-packages-config "Direct link to detecting-changes-in-packages-config")
The `package-lock.yml` file includes a `sha1_hash` of your packages config. If you update `packages.yml`, dbt will detect the change and rerun dependency resolution during the next `dbt deps` command. To update the lock file without installing the new packages, use the `--lock` flag:
```
dbt deps --lock
```

### Forcing package updates[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#forcing-package-updates "Direct link to Forcing package updates")
To update all packages, even if `packages.yml` hasn't changed, use the `--upgrade` flag:
```
dbt deps --upgrade
```

This is particularly useful for fetching the latest commits from the `main` branch of an internally maintained Git package.
Forcing package upgrades may introduce build inconsistencies unless carefully managed.
### Adding specific packages[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#adding-specific-packages "Direct link to Adding specific packages")
The `dbt deps` command can add or update package configurations directly, saving you from remembering exact syntax.
#### Hub packages (default)[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#hub-packages-default "Direct link to Hub packages \(default\)")
Hub packages are the default package types and the easiest to install.
```
dbt deps --add-package dbt-labs/dbt_utils@1.0.0# with semantic version rangedbt deps --add-package dbt-labs/snowplow@">=0.7.0,<0.8.0"
```

#### Non-Hub packages[​](https://docs.getdbt.com/reference/commands/deps?version=1.12#non-hub-packages "Direct link to Non-Hub packages")
Use the `--source` flag to specify the type of package to be installed:
```
# Git packagedbt deps --add-package https://github.com/fivetran/dbt_amplitude@v0.3.0 --sourcegit# Local packagedbt deps --add-package /opt/dbt/redshift --sourcelocal
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/clone ---

[Skip to main content](https://docs.getdbt.com/reference/commands/clone?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fclone+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fclone+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fclone+so+I+can+ask+questions+about+it.)
On this page
The `dbt clone` command clones selected nodes from the [specified state](https://docs.getdbt.com/reference/node-selection/syntax#establishing-state) to the target schema(s). This command makes use of the `clone` materialization:
  * If your data platform supports zero-copy cloning of tables (Snowflake, Databricks, or BigQuery), and this model exists as a table in the source environment, dbt will create it in your target environment as a clone.
  * Otherwise, dbt will create a simple pointer view (`select * from` the source object)
  * By default, `dbt clone` will not recreate pre-existing relations in the current target. To override this, use the `--full-refresh` flag.
  * You may want to specify a higher number of [threads](https://docs.getdbt.com/docs/running-a-dbt-project/using-threads) to decrease execution time since individual clone statements are independent of one another.


The `clone` command is useful for:
  * blue/green continuous deployment (on data warehouses that support zero-copy cloning tables)
  * cloning current production state into development schema(s)
  * handling incremental models in dbt CI jobs (on data warehouses that support zero-copy cloning tables)
  * testing code changes on downstream dependencies in your BI tool


```
# clone all of my models from specified state to my target schema(s)dbt clone --state path/to/artifacts# clone one_specific_model of my models from specified state to my target schema(s)dbt clone --select"one_specific_model"--state path/to/artifacts# clone all of my models from specified state to my target schema(s) and recreate all pre-existing relations in the current targetdbt clone --state path/to/artifacts --full-refresh# clone all of my models from specified state to my target schema(s), running up to 50 clone statements in paralleldbt clone --state path/to/artifacts --threads50
```

### When to use `dbt clone` instead of [deferral](https://docs.getdbt.com/reference/node-selection/defer)?[​](https://docs.getdbt.com/reference/commands/clone?version=1.12#when-to-use-dbt-clone-instead-of-deferral "Direct link to when-to-use-dbt-clone-instead-of-deferral")
Unlike deferral, `dbt clone` requires some compute and creation of additional objects in your data warehouse. In many cases, deferral is a cheaper and simpler alternative to `dbt clone`. However, `dbt clone` covers additional use cases where deferral may not be possible.
For example, by creating actual data warehouse objects, `dbt clone` allows you to test out your code changes on downstream dependencies _outside of dbt_ (such as a BI tool).
As another example, you could `clone` your modified incremental models as the first step of your dbt CI job to prevent costly `full-refresh` builds for warehouses that support zero-copy cloning.
## Cloning in dbt[​](https://docs.getdbt.com/reference/commands/clone?version=1.12#cloning-in-dbt "Direct link to Cloning in dbt")
You can clone nodes between states in dbt using the `dbt clone` command. This is available in the [Studio IDE](https://docs.getdbt.com/docs/cloud/studio-ide/develop-in-studio) and the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation) and relies on the [`--defer`](https://docs.getdbt.com/reference/node-selection/defer) feature. For more details on defer in dbt, read [Using defer in dbt](https://docs.getdbt.com/docs/cloud/about-cloud-develop-defer).
  * **Using dbt CLI** — The `dbt clone` command in the dbt CLI automatically includes the `--defer` flag. This means you can use the `dbt clone` command without any additional setup.
  * **Using Studio IDE** — To use the `dbt clone` command in the Studio IDE, follow these steps before running the `dbt clone` command:
    * Set up your **Production environment** and have a successful job run.
    * Enable **Defer to production** by toggling the switch in the lower-right corner of the command bar.
Select the 'Defer to production' toggle on the bottom right of the command bar to enable defer in the Studio IDE.
    * Run the `dbt clone` command from the command bar.


Check out [this Developer blog post](https://docs.getdbt.com/blog/to-defer-or-to-clone) for more details on best practices when to use `dbt clone` vs. deferral.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/catalog-json ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/catalog-json?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fcatalog-json+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fcatalog-json+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fcatalog-json+so+I+can+ask+questions+about+it.)
On this page
**Current schema** :
**Produced by:** [`docs generate`](https://docs.getdbt.com/reference/commands/cmd-docs)
This file contains information from your data warehouseviewstable[docs site](https://docs.getdbt.com/docs/explore/build-and-view-your-docs).
### Top-level keys[​](https://docs.getdbt.com/reference/artifacts/catalog-json?version=1.12#top-level-keys "Direct link to Top-level keys")
  * `nodes`: Dictionary containing information about database objects corresponding to dbt models, seeds, and snapshots.
  * `sources`: Dictionary containing information about database objects corresponding to dbt sources.
  * `errors`: Errors received while running metadata queries during `dbt docs generate`.


### Resource details[​](https://docs.getdbt.com/reference/artifacts/catalog-json?version=1.12#resource-details "Direct link to Resource details")
Within `sources` and `nodes`, each dictionary key is a resource `unique_id`. Each nested resource contains:
  * `unique_id`: `<resource_type>.<package>.<resource_name>`, same as dictionary key, maps to `nodes` and `sources` in the [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json)
  * `metadata`
    * `type`: table, view, etc.
    * `database`
    * `schema`
    * `name`
    * `comment`
    * `owner`
  * `columns` (array)
    * `name`
    * `type`: data type
    * `comment`
    * `index`: ordinal
  * `stats`: differs by database and relation type


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Was this page helpful?](https://docs.getdbt.com/reference/artifacts/catalog-json?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/changes-overview ---

[Skip to main content](https://docs.getdbt.com/reference/changes-overview?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fchanges-overview+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fchanges-overview+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fchanges-overview+so+I+can+ask+questions+about+it.)
When using dbt, you may see warnings or other changes that need your attention. These changes help us move forward with the latest version of dbt and improve the experience for all users.
Use this page to understand the different types of changes, what to do, and where to find more information.
#### [Deprecations Features in your project code (models, YAML, macros) that still work but will be removed.**Impact:** Currently warnings; will cause errors in future versions.**Action:** Update your project code to use the new syntax.](https://docs.getdbt.com/reference/deprecations)
#### [Behavior change flags Settings in your dbt_project.yml file that let you opt in or out of new behaviors during migration periods.**Impact:** Controls whether dbt uses old or new behavior; defaults change over time.**Action:** Set flags to control timing of adoption.](https://docs.getdbt.com/reference/global-configs/behavior-changes)
#### [Deprecated CLI flags Command-line flags passed to dbt commands that are being removed in Fusion.**Impact:** Some ignored (with warnings); **--models** flag will error in Fusion.**Action:** Update job definitions and scripts to remove or replace these flags.](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-fusion#deprecated-flags)
## Preparing for Fusion[​](https://docs.getdbt.com/reference/changes-overview?version=1.12#preparing-for-fusion "Direct link to Preparing for Fusion")
If you're upgrading to Fusion, you should:
  * Resolve all [deprecations](https://docs.getdbt.com/reference/deprecations) to avoid causing errors in Fusion.
  * Review [behavior change flags](https://docs.getdbt.com/reference/global-configs/behavior-changes) to understand how Fusion will behave (new behavior is always enabled).
  * Update [deprecated CLI flags](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-fusion#deprecated-flags) to avoid errors in Fusion.


## Related docs[​](https://docs.getdbt.com/reference/changes-overview?version=1.12#related-docs "Direct link to Related docs")
  * [Full deprecations list](https://docs.getdbt.com/reference/deprecations)
  * [Behavior change flags](https://docs.getdbt.com/reference/global-configs/behavior-changes)
  * [Upgrading to Fusion](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/upgrading-to-fusion)
  * [Fusion readiness checklist](https://docs.getdbt.com/docs/fusion/fusion-readiness)
  * [Events and logging](https://docs.getdbt.com/reference/events-logging)


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/parse ---

[Skip to main content](https://docs.getdbt.com/reference/commands/parse?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fparse+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fparse+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fparse+so+I+can+ask+questions+about+it.)
The `dbt parse` command parses and validates the contents of your dbt project. If your project contains Jinja or YAML syntax errors, the command will fail.
It will also produce an artifact with detailed timing information, which is useful to understand parsing times for large projects. Refer to [Project parsing](https://docs.getdbt.com/reference/parsing) for more information.
Starting in v1.5, `dbt parse` will write or return a [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json), enabling you to introspect dbt's understanding of all the resources in your project. Since `dbt parse` doesn't connect to your warehouse, [this manifest will not contain any compiled code](https://docs.getdbt.com/faqs/Warehouse/db-connection-dbt-compile).
By default, the Studio IDE will attempt a "partial" parse, which means it'll only check changes since the last parse (new or updated parts of your project when you make changes). Since the Studio IDE automatically parses in the background whenever you save your work, manually running `dbt parse` yourself is likely to be fast because it's just looking at recent changes.
As an option, you can tell dbt to check the entire project from scratch by using the `--no-partial-parse` flag. This makes dbt perform a full re-parse of the project, not just the recent changes.
```
$ dbt parse13:02:52  Running with dbt=1.5.013:02:53  Performance info: target/perf_info.json
```

target/perf_info.json
```
"path_count":7,"is_partial_parse_enabled":false,"parse_project_elapsed":0.20151838900000008,"patch_sources_elapsed":0.00039490800000008264,"process_manifest_elapsed":0.029363873999999957,"load_all_elapsed":0.240095269,"projects":["project_name":"my_project","elapsed":0.07518750299999999,"parsers":["parser":"model","elapsed":0.04545303199999995,"path_count":1"parser":"operation","elapsed":0.0006415469999998535,"path_count":1"parser":"seed","elapsed":0.026538173000000054,"path_count":2"path_count":4"project_name":"dbt_postgres","elapsed":0.0016448299999998195,"parsers":["parser":"operation","elapsed":0.00021672399999994596,"path_count":1"path_count":1"project_name":"dbt","elapsed":0.006580432000000025,"parsers":["parser":"operation","elapsed":0.0002488560000000195,"path_count":1"parser":"docs","elapsed":0.002500640000000054,"path_count":1"path_count":2
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/manifest-json ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/manifest-json#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fmanifest-json+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fmanifest-json+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fmanifest-json+so+I+can+ask+questions+about+it.)
On this page
dbt version | Manifest version
---|---
dbt Fusion engine v2.0 | v20 (Identical to [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html))
Core v1.11
Core v1.10
Core v1.9
Core v1.8
Core v1.7
Core v1.6
Core v1.5
Core v1.4
Core v1.3
Loading table...
---
**Produced by** : Any [dbt command](https://docs.getdbt.com/category/list-of-commands) that parses the project. This includes all commands, _except_ [`deps`](https://docs.getdbt.com/reference/commands/deps), [`clean`](https://docs.getdbt.com/reference/commands/clean), [`debug`](https://docs.getdbt.com/reference/commands/debug), and [`init`](https://docs.getdbt.com/reference/commands/init).
After executing a dbt command, the `manifest.json` file can be found in the project's `target/` directory:
  * If developing locally: Open the `target/` directory in your project folder
  * In the Studio IDE: Open the `target/` directory in the file tree
  * In dbt platform jobs: Download the `manifest.json` from the [artifacts](https://docs.getdbt.com/reference/artifacts/dbt-artifacts) tab for a given job run


This file contains a full representation of your dbt project's resources (models, tests, macros, and more), including all node configurations and resource properties. Even if you're only running some models or tests, all resources will appear in the manifest (unless they are disabled) with most of their properties. Some properties, such as `compiled_sql`, are included only for executed nodes.
Today, dbt uses this file to populate the [docs site](https://docs.getdbt.com/docs/explore/build-and-view-your-docs), and to perform [state comparison](https://docs.getdbt.com/reference/node-selection/syntax#about-node-selection). Members of the community also use it to analyze project health, such as checking for missing descriptions or tests.
### Top-level keys[​](https://docs.getdbt.com/reference/artifacts/manifest-json#top-level-keys "Direct link to Top-level keys")
  * `nodes`: Dictionary of all analyses, models, seeds, snapshots, and tests.
  * `sources`: Dictionary of sources
  * `metrics`: Dictionary of metrics
  * `exposures`: Dictionary of exposures
  * `groups`: Dictionary of groups (**Note:** Added in v1.5)
  * `macros`: Dictionary of macros
  * `docs`: Dictionary of `docs` blocks
  * `parent_map`: Dictionary that contains the first-order parents of each resource
  * `child_map`: Dictionary that contains the first-order children of each resource
  * `group_map`: Dictionary that maps group names to their resource nodes
  * `selectors`: Expanded dictionary representation of [YAML `selectors`](https://docs.getdbt.com/reference/node-selection/yaml-selectors)
  * `disabled`: Array of resources with `enabled: false`


### Resource details[​](https://docs.getdbt.com/reference/artifacts/manifest-json#resource-details "Direct link to Resource details")
All resources nested within `nodes`, `sources`, `metrics`, `exposures`, `macros`, and `docs` have the following base properties:
  * `name`: Resource name
  * `unique_id`: `<resource_type>.<package>.<resource_name>`, same as dictionary key
  * `package_name`: Name of package that defines this resource
  * `root_path`: Absolute file path of this resource's package. (**Note:** This was removed for most node types in dbt Core v1.4 / manifest v8 to reduce duplicative information across nodes, but it is still present for seeds.)
  * `path`: Relative file path of this resource's definition within its "resource path" (`model-paths`, `seed-paths`, and more).
  * `original_file_path`: Relative file path of this resource's definition, including its resource path.


Each has several additional properties related to its resource type.
### dbt JSON schema[​](https://docs.getdbt.com/reference/artifacts/manifest-json#dbt-json-schema "Direct link to dbt JSON schema")
You can refer to the [dbt JSON schema](https://schemas.getdbt.com/) for information on describing and consuming dbt-generated artifacts.
**Note** : The `manifest.json` version number is related to (but not _equal_ to) your dbt version, so you _must_ use the correct `manifest.json` version for your dbt version. To find the correct `manifest.json` version, select the dbt version on the top navigation (such as `v1.5`).
Refer to the table at the beginning of [this page](https://docs.getdbt.com/reference/artifacts/manifest-json) to understand how the manifest version matches the dbt version.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12 ---

[Skip to main content](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fdbt-artifacts+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fdbt-artifacts+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fartifacts%2Fdbt-artifacts+so+I+can+ask+questions+about+it.)
On this page
With every invocation, dbt generates and saves one or more _artifacts_. Several of these are JSON`semantic_manifest.json`, `manifest.json`, `catalog.json`, `run_results.json`, and `sources.json`) that are used to power:
  * [visualizing source freshness](https://docs.getdbt.com/docs/build/sources#source-data-freshness)


They could also be used to:
  * gain insights into your [Semantic Layer](https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl)
  * calculate project-level test coverage
  * perform longitudinal analysis of run timing
  * identify historical changes in table
  * do much, much more


### When are artifacts produced? [Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#when-are-artifacts-produced- "Direct link to when-are-artifacts-produced-")
Most dbt commands (and corresponding RPC methods) produce artifacts:
  * [semantic manifest](https://docs.getdbt.com/reference/artifacts/sl-manifest): produced whenever your dbt project is parsed
  * [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json): produced by commands that read and understand your project
  * [run results](https://docs.getdbt.com/reference/artifacts/run-results-json): produced by commands that run, compile, or catalog nodes in your DAG
  * [catalog](https://docs.getdbt.com/reference/artifacts/catalog-json): produced by `docs generate`
  * [sources](https://docs.getdbt.com/reference/artifacts/sources-json): produced by `source freshness`


When running commands from the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation), all artifacts are downloaded by default. If you want to change this behavior, refer to [How to skip artifacts from being downloaded](https://docs.getdbt.com/docs/cloud/configure-cloud-cli#how-to-skip-artifacts-from-being-downloaded).
## Where are artifacts produced?[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#where-are-artifacts-produced "Direct link to Where are artifacts produced?")
By default, artifacts are written to the `/target` directory of your dbt project. You can configure the location using the [`target-path` flag](https://docs.getdbt.com/reference/global-configs/json-artifacts).
## Common metadata[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#common-metadata "Direct link to Common metadata")
All artifacts produced by dbt include a `metadata` dictionary with these properties:
  * `dbt_version`: Version of dbt that produced this artifact. For details about release versioning, refer to [Versioning](https://docs.getdbt.com/reference/commands/version#versioning).
  * `dbt_schema_version`: URL of this artifact's schema. See notes below.
  * `generated_at`: Timestamp in UTC when this artifact was produced.
  * `adapter_type`: The adapter (database), e.g. `postgres`, `spark`, etc.
  * `env`: Any environment variables prefixed with `DBT_ENV_CUSTOM_ENV_` will be included in a dictionary, with the prefix-stripped variable name as its key.
  * [`invocation_id`](https://docs.getdbt.com/reference/dbt-jinja-functions/invocation_id): Unique identifier for this dbt invocation


In the manifest, the `metadata` may also include:
  * `send_anonymous_usage_stats`: Whether this invocation sent [anonymous usage statistics](https://docs.getdbt.com/reference/global-configs/usage-stats) while executing.
  * `project_name`: The `name` defined in the root project's `dbt_project.yml`. (Added in manifest v10 / dbt Core v1.6)
  * `project_id`: Project identifier, hashed from `project_name`, sent with anonymous usage stats if enabled.
  * `user_id`: User identifier, stored by default in `~/dbt/.user.yml`, sent with anonymous usage stats if enabled.


#### Notes:[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#notes "Direct link to Notes:")
  * The structure of dbt artifacts is canonized by [JSON schemas](https://json-schema.org/), which are hosted at [schemas.getdbt.com](https://schemas.getdbt.com/).
  * Artifact versions may change in any minor version of dbt (`v1.x.0`). Each artifact is versioned independently.


## Related docs[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#related-docs "Direct link to Related docs")
  * [Other artifacts](https://docs.getdbt.com/reference/artifacts/other-artifacts) files such as `index.html` or `graph_summary.json`.


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [When are artifacts produced? ](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#when-are-artifacts-produced)[Starter](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[Enterprise](https://www.getdbt.com/pricing "Go to https://www.getdbt.com/pricing")[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#when-are-artifacts-produced- "Direct link to when-are-artifacts-produced-")
  * [Where are artifacts produced?](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#where-are-artifacts-produced)[​](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#where-are-artifacts-produced "Direct link to Where are artifacts produced?")
  * [Was this page helpful?](https://docs.getdbt.com/reference/artifacts/dbt-artifacts?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/invocation ---

[Skip to main content](https://docs.getdbt.com/reference/commands/invocation?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Finvocation+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Finvocation+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Finvocation+so+I+can+ask+questions+about+it.)
On this page
The `dbt invocation` command is available in the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation) and allows you to:
  * List active invocations to debug long-running or hanging invocations.
  * Identify and investigate sessions causing the `Session occupied` error.
  * Monitor currently active dbt commands (like `run`, `build`) in real-time.


The `dbt invocation` command only lists _active invocations_. If no sessions are running, the list will be empty. Completed sessions aren't included in the output.
## Usage[​](https://docs.getdbt.com/reference/commands/invocation?version=1.12#usage "Direct link to Usage")
This page lists the command and flag you can use with `dbt invocation`. To use them, add a command or option like this: `dbt invocation [command]`.
Available flags in the command line interface (CLI) are [`help`](https://docs.getdbt.com/reference/commands/invocation?version=1.12#dbt-invocation-help) and [`list`](https://docs.getdbt.com/reference/commands/invocation?version=1.12#dbt-invocation-list).
### dbt invocation help[​](https://docs.getdbt.com/reference/commands/invocation?version=1.12#dbt-invocation-help "Direct link to dbt invocation help")
The `help` command provides you with the help output for the `invocation` command in the CLI, including the available flags.
```
dbt invocation help
```

or
```
dbt help invocation
```

The command returns the following information:
```
dbt invocation helpManage invocationsUsage:  dbt invocation [command]Available Commands:  list        List active invocationsFlags:  -h, --helphelpfor invocationGlobal Flags:      --log-format LogFormat   The log format, either json or plain. (default plain)      --log-level LogLevel     The log level, one of debug, info, warning, error or fatal. (default info)      --no-color               Disables colorization of the output.  -q, --quiet                  Suppress all non-error logging to stdout.Use "dbt invocation [command] --help"formore information about a command.
```

### dbt invocation list[​](https://docs.getdbt.com/reference/commands/invocation?version=1.12#dbt-invocation-list "Direct link to dbt invocation list")
The `list` command provides you with a list of active invocations in your dbt CLI. When a long-running session is active, you can use this command in a separate terminal window to view the active session to help debug the issue.
```
dbt invocation list
```

The command returns the following information, including the `ID`, `status`, `type`, `arguments`, and `started at` time of the active session:
```
dbt invocation listActive Invocations:  ID                             6dcf4723-e057-48b5-946f-a4d87e1d117a  Status                         running  Type                           cli[run --select test.sql]  Started At                     2025-01-24 11:03:19➜  jaffle-shop git:(test-cli)
```

To cancel an active session in the terminal, use the `Ctrl + Z` shortcut.
## Related docs[​](https://docs.getdbt.com/reference/commands/invocation?version=1.12#related-docs "Direct link to Related docs")
  * [Install dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation)
  * [Troubleshooting dbt CLI 'Session occupied' error](https://docs.getdbt.com/faqs/Troubleshooting/long-sessions-cloud-cli)


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Usage](https://docs.getdbt.com/reference/commands/invocation?version=1.12#usage)[​](https://docs.getdbt.com/reference/commands/invocation?version=1.12#usage "Direct link to Usage")
  * [Was this page helpful?](https://docs.getdbt.com/reference/commands/invocation?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/compile ---

[Skip to main content](https://docs.getdbt.com/reference/commands/compile#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fcompile+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fcompile+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fcompile+so+I+can+ask+questions+about+it.)
On this page
`dbt compile` generates executable SQL from source `model`, `test`, and `analysis` files. You can find these compiled SQL files in the `target/` directory of your dbt project.
The `compile` command is useful for:
  1. Visually inspecting the compiled output of model files. This is useful for validating complex Jinja logic or macro usage.
  2. Manually running compiled SQL. While debugging a model or schema test, it's often useful to execute the underlying `select` statement to find the source of the bug.
  3. Compiling `analysis` files. Read more about analysis files [here](https://docs.getdbt.com/docs/build/analyses).


Some common misconceptions:
  * `dbt compile` is _not_ a pre-requisite of `dbt run`, or other building commands. Those commands will handle compilation themselves.
  * If you just want dbt to read and validate your project code, without connecting to the data warehouse, use `dbt parse` instead.


### Interactive compile[​](https://docs.getdbt.com/reference/commands/compile#interactive-compile "Direct link to Interactive compile")
Starting in dbt v1.5, `compile` can be "interactive" in the CLI, by displaying the compiled code of a node or arbitrary dbt-SQL query:
  * `--select` a specific node _by name_
  * `--inline` an arbitrary dbt-SQL query


This will log the compiled SQL to the terminal, in addition to writing to the `target/` directory.
For example:
```
dbt compile --select"stg_orders"dbt compile --inline"select * from {{ ref('raw_orders') }}"
```

returns the following:
```
dbt compile --select"stg_orders"21:17:09  Running with dbt=1.7.521:17:09  Registered adapter: postgres=1.7.521:17:09  Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 401 macros, 0 groups, 0 semantic models21:17:09  21:17:09 Concurrency: 24 threads (target='dev')21:17:09  21:17:09  Compiled node'stg_orders' is:with source as (select * from "jaffle_shop"."main"."raw_orders"renamed as (selectid as order_id,        user_id as customer_id,        order_date,        status    from sourceselect * from renamed
```

```
dbt compile --inline"select * from {{ ref('raw_orders') }}"18:15:49  Running with dbt=1.7.518:15:50  Registered adapter: postgres=1.7.518:15:50  Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 401 macros, 0 groups, 0 semantic models18:15:50  18:15:50  Concurrency: 5 threads (target='postgres')18:15:50  18:15:50  Compiled inline node is:select * from "jaffle_shop"."main"."raw_orders"
```

The command accesses the data platform to cache-related metadata, and to run introspective queries. Use the flags:
  * `--no-populate-cache` to disable the initial cache population. If metadata is needed, it will be a cache miss, requiring dbt to run the metadata query. This is a `dbt` flag, which means you need to add `dbt` as a prefix. For example: `dbt --no-populate-cache`.
  * `--no-introspect` to disable [introspective queries](https://docs.getdbt.com/faqs/Warehouse/db-connection-dbt-compile#introspective-queries). dbt will raise an error if a model's definition requires running one. This is a `dbt compile` flag, which means you need to add `dbt compile` as a prefix. For example:`dbt compile --no-introspect`.


### FAQs[​](https://docs.getdbt.com/reference/commands/compile#faqs "Direct link to FAQs")
Why dbt compile needs a data platform connection
`dbt compile` needs a data platform connection in order to gather the info it needs (including from introspective queries) to prepare the SQL for every model in your project.
### dbt compile[​](https://docs.getdbt.com/reference/commands/compile#dbt-compile "Direct link to dbt compile")
The [`dbt compile` command](https://docs.getdbt.com/reference/commands/compile) generates executable SQL from `source`, `model`, `test`, and `analysis` files. `dbt compile` is similar to `dbt run` except that it doesn't materialize the model's compiled SQL into an existing table. So, up until the point of materialization, `dbt compile` and `dbt run` are similar because they both require a data platform connection, run queries, and have an [`execute` variable](https://docs.getdbt.com/reference/dbt-jinja-functions/execute) set to `True`.
However, here are some things to consider:
  * You don't need to execute `dbt compile` before `dbt run`
  * In dbt, `compile` doesn't mean `parse`. This is because `parse` validates your written `YAML`, configured tags, and so on.


### Introspective queries[​](https://docs.getdbt.com/reference/commands/compile#introspective-queries "Direct link to Introspective queries")
To generate the compiled SQL for many models, dbt needs to run introspective queries, (which is when dbt needs to run SQL in order to pull data back and do something with it) against the data platform.
These introspective queries include:
  * Populating the relation cache. For more information, refer to the [Create new materializations](https://docs.getdbt.com/guides/create-new-materializations) guide. Caching speeds up the metadata checks, including whether an [incremental model](https://docs.getdbt.com/docs/build/incremental-models) already exists in the data platform.
  * Resolving [macros](https://docs.getdbt.com/docs/build/jinja-macros#macros), such as `run_query` or `dbt_utils.get_column_values` that you're using to template out your SQL. This is because dbt needs to run those queries during model SQL compilation.


Without a data platform connection, dbt can't perform these introspective queries and won't be able to generate the compiled SQL needed for the next steps in the dbt workflow. You can [`parse`](https://docs.getdbt.com/reference/commands/parse) a project and use the [`list`](https://docs.getdbt.com/reference/commands/list) resources in the project, without an internet or data platform connection. Parsing a project is enough to produce a [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json), however, keep in mind that the written-out manifest won't include compiled SQL.
To configure a project, you do need a [connection profile](https://docs.getdbt.com/docs/local/profiles.yml) (`profiles.yml` if using the CLI). You need this file because the project's configuration depends on its contents. For example, you may need to use [`{{target}}`](https://docs.getdbt.com/reference/dbt-jinja-functions/target) for conditional configs or know what platform you're running against so that you can choose the right flavor of SQL.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/list ---

[Skip to main content](https://docs.getdbt.com/reference/commands/list?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Flist+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Flist+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Flist+so+I+can+ask+questions+about+it.)
On this page
The `dbt ls` command lists resources in your dbt project. It accepts selector arguments that are similar to those provided in [dbt run](https://docs.getdbt.com/reference/commands/run). `dbt list` is an alias for `dbt ls`. While `dbt ls` will read your [connection profile](https://docs.getdbt.com/docs/local/profiles.yml) to resolve [`target`](https://docs.getdbt.com/reference/dbt-jinja-functions/target)-specific logic, this command will not connect to your database or run any queries.
### Usage[​](https://docs.getdbt.com/reference/commands/list?version=1.12#usage "Direct link to Usage")
```
dbt ls     [--resource-type {model,semantic_model,source,seed,snapshot,metric,test,exposure,analysis,function,default,all}]     [--select SELECTION_ARG [SELECTION_ARG ...]]     [--models SELECTOR [SELECTOR ...]]     [--exclude SELECTOR [SELECTOR ...]]     [--selector YML_SELECTOR_NAME]     [--output {json,name,path,selector}]     [--output-keys KEY_NAME [KEY_NAME]]
```

See [resource selection syntax](https://docs.getdbt.com/reference/node-selection/syntax) for more information on how to select resources in dbt
**Arguments** :
  * `--resource-type`: This flag restricts the "resource types" returned by dbt in the `dbt ls` command. By default, all resource types are included in the results of `dbt ls` except for the analysis type.
  * `--select`: This flag specifies one or more selection-type arguments used to filter the nodes returned by the `dbt ls` command
  * `--models`: Like the `--select` flag, this flag is used to select nodes. It implies `--resource-type=model`, and will only return models in the results of the `dbt ls` command. Supported for backwards compatibility only.
  * `--exclude`: Specify selectors that should be _excluded_ from the list of returned nodes.
  * `--selector`: This flag specifies one named selector, defined in a `selectors.yml` file.
  * `--output`: This flag controls the format of output from the `dbt ls` command.
  * `--output-keys`: If `--output json`, this flag controls which node properties are included in the output.


Note that the `dbt ls` command does not include models which are disabled or schema tests which depend on models which are disabled. All returned resources will have a `config.enabled` value of `true`.
### Example usage[​](https://docs.getdbt.com/reference/commands/list?version=1.12#example-usage "Direct link to Example usage")
The following examples show how to use the `dbt ls` command to list resources in your project.
  * [Listing models by package](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-models-by-package)
  * [Listing tests by tag name](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-tests-by-tag-name)
  * [Listing schema tests of incremental models](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-schema-tests-of-incremental-models)
  * [Listing JSON output](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-json-output)
  * [Listing JSON output with custom keys](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-json-output-with-custom-keys)
  * [Listing semantic models](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-semantic-models)
  * [Listing functions](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-functions)


#### Listing models by package[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-models-by-package "Direct link to Listing models by package")
```
dbt ls--select snowplow.*snowplow.snowplow_base_eventssnowplow.snowplow_base_web_page_contextsnowplow.snowplow_id_mapsnowplow.snowplow_page_viewssnowplow.snowplow_sessions
```

#### Listing tests by tag name[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-tests-by-tag-name "Direct link to Listing tests by tag name")
```
dbt ls--select tag:nightly --resource-type testmy_project.schema_test.not_null_orders_order_idmy_project.schema_test.unique_orders_order_idmy_project.schema_test.not_null_products_product_idmy_project.schema_test.unique_products_product_id
```

#### Listing schema tests of incremental models[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-schema-tests-of-incremental-models "Direct link to Listing schema tests of incremental models")
```
dbt ls--select config.materialized:incremental,test_type:schemamodel.my_project.logs_parsedmodel.my_project.events_categorized
```

#### Listing JSON output[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-json-output "Direct link to Listing JSON output")
```
dbt ls--select snowplow.* --output json{"name":"snowplow_events", "resource_type":"model", "package_name":"snowplow"...}{"name":"snowplow_page_views", "resource_type":"model", "package_name":"snowplow"...}
```

#### Listing JSON output with custom keys[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-json-output-with-custom-keys "Direct link to Listing JSON output with custom keys")
```
dbt ls--select snowplow.* --output json --output-keys "name resource_type description"{"name":"snowplow_events", "description":"This is a pretty cool model"...}{"name":"snowplow_page_views", "description":"This model is even cooler"...}
```

#### Listing semantic models[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-semantic-models "Direct link to Listing semantic models")
List all resources upstream of your orders semantic model:
```
dbt ls-s +semantic_model:orders
```

#### Listing file paths[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-file-paths "Direct link to Listing file paths")
```
dbt ls--select snowplow.* --output pathmodels/base/snowplow_base_events.sqlmodels/base/snowplow_base_web_page_context.sqlmodels/identification/snowplow_id_map.sql
```

#### Listing functions[​](https://docs.getdbt.com/reference/commands/list?version=1.12#listing-functions "Direct link to Listing functions")
List all functions in your project:
```
dbt list --select"resource_type:function"# or dbt ls --resource-type functionjaffle_shop.area_of_circlejaffle_shop.whoami
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/retry ---

[Skip to main content](https://docs.getdbt.com/reference/commands/retry?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fretry+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fretry+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fretry+so+I+can+ask+questions+about+it.)
`dbt retry` re-executes the last `dbt` command from the node point of failure.
  * If no nodes are executed before the failure (for example, if a run failed early due to a warehouse connection or permission errors), `dbt retry` won't run anything since there's no recorded nodes to retry from.
  * In these cases, we recommend checking your [`run_results.json` file](https://docs.getdbt.com/reference/artifacts/run-results-json) and manually re-running the full job so the nodes build.
  * Once some nodes have run, you can use `dbt retry` to re-execute from any new point of failure.
  * If the previously executed command completed successfully, `dbt retry` will finish as `no operation`.


Retry works with the following commands:


`dbt retry` references [run_results.json](https://docs.getdbt.com/reference/artifacts/run-results-json) to determine where to start. Executing `dbt retry` without correcting the previous failures will garner idempotent
`dbt retry` reuses the [selectors](https://docs.getdbt.com/reference/node-selection/yaml-selectors) from the previously executed command.
Example results of executing `dbt retry` after a successful `dbt run`:
```
Running with dbt=1.6.1Registered adapter: duckdb=1.6.0Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 348 macros, 0 groups, 0 semantic modelsNothing to do. Try checking your model configs and model specification args
```

Example of when `dbt run` encounters a syntax error in a model:
```
Running with dbt=1.6.1Registered adapter: duckdb=1.6.0Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 348 macros, 0 groups, 0 semantic modelsConcurrency: 24 threads (target='dev')1 of 5 START sql view model main.stg_customers ................................. [RUN]2 of 5 START sql view model main.stg_orders ....................................[RUN]3 of 5 START sql view model main.stg_payments ..................................[RUN]1 of 5 OK created sql view model main.stg_customers ............................[OK in0.06s]2 of 5 OK created sql view model main.stg_orders ............................... [OK in0.06s]3 of 5 OK created sql view model main.stg_payments ............................. [OK in0.07s]4 of 5 START sql table model main.customers ....................................[RUN]5 of 5 START sql table model main.orders ....................................... [RUN]4 of 5 ERROR creating sql table model main.customers ........................... [ERROR in0.03s]5 of 5 OK created sql table model main.orders ..................................[OK in0.04s]Finished running 3 view models, 2 table models in0 hours 0 minutes and 0.15 seconds (0.15s).Completed with 1 error and 0 warnings:Runtime Error in model customers (models/customers.sql) Parser Error: syntax error at or near "selct"Done. PASS=4WARN=0ERROR=1SKIP=0TOTAL=5
```

Example of a subsequent failed `dbt retry` run without fixing the error(s):
```
Running with dbt=1.6.1Registered adapter: duckdb=1.6.0Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 348 macros, 0 groups, 0 semantic modelsConcurrency: 24 threads (target='dev')1 of 1 START sql table model main.customers ....................................[RUN]1 of 1 ERROR creating sql table model main.customers ........................... [ERROR in0.03s]Done. PASS=4WARN=0ERROR=1SKIP=0TOTAL=5
```

Example of a successful `dbt retry` run after fixing error(s):
```
Running with dbt=1.6.1Registered adapter: duckdb=1.6.0Found 5 models, 3 seeds, 20 tests, 0 sources, 0 exposures, 0 metrics, 348 macros, 0 groups, 0 semantic modelsConcurrency: 24 threads (target='dev')1 of 1 START sql table model main.customers ....................................[RUN]1 of 1 OK created sql table model main.customers ............................... [OK in0.05s]Finished running 1 table model in0 hours 0 minutes and 0.09 seconds (0.09s).Completed successfullyDone. PASS=1WARN=0ERROR=0SKIP=0TOTAL=1
```

In each scenario `dbt retry` picks up from the error rather than running all of the upstream dependencies again.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/run ---

[Skip to main content](https://docs.getdbt.com/reference/commands/run?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Frun+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Frun+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Frun+so+I+can+ask+questions+about+it.)
On this page
## Overview[​](https://docs.getdbt.com/reference/commands/run?version=1.12#overview "Direct link to Overview")
The `dbt run` command only applies to models. It doesn't run tests, snapshots, seeds, or other resource types. To run those commands, use the appropriate dbt commands found in the [dbt commands](https://docs.getdbt.com/reference/dbt-commands) section — such as `dbt test`, `dbt snapshot`, or `dbt seed`. Alternatively, use `dbt build` with a [resource type selector](https://docs.getdbt.com/reference/node-selection/methods#resource_type).
You can use the `dbt run` command when you want to build or rebuild models in your project.
### How does `dbt run` work?[​](https://docs.getdbt.com/reference/commands/run?version=1.12#how-does-dbt-run-work "Direct link to how-does-dbt-run-work")
  * `dbt run` executes compiled SQL model files against the current `target` database.
  * dbt connects to the target database and runs the relevant SQL required to materialize all data models using the specified materialization
  * Models are run in the order defined by the dependency graph generated during compilation. Intelligent multi-threading is used to minimize execution time without violating dependencies.
  * Deploying new models frequently involves destroying prior versions of these models. In these cases, `dbt run` minimizes downtime by first building each model with a temporary name, then dropping and renaming within a single transaction (for adapters that support transactions).


## Refresh incremental models[​](https://docs.getdbt.com/reference/commands/run?version=1.12#refresh-incremental-models "Direct link to Refresh incremental models")
If you provide the `--full-refresh` flag to `dbt run`, dbt will treat incremental models as table
  1. The schema of an incremental model changes and you need to recreate it.
  2. You want to reprocess the entirety of the incremental model because of new logic in the model code.


bash
```
dbt run --full-refresh
```

You can also supply the flag by its short name: `dbt run -f`.
In the dbt compilation context, this flag will be available as [flags.FULL_REFRESH](https://docs.getdbt.com/reference/dbt-jinja-functions/flags). Further, the `is_incremental()` macro will return `false` for _all_ models in response when the `--full-refresh` flag is specified.
models/example.sql
```
select*from all_events-- if the table already exists and `--full-refresh` is-- not set, then only add new records. otherwise, select-- all records.{%if is_incremental()%}where collector_tstamp (selectcoalesce(max(max_tstamp),'0001-01-01')from {{ this }}{% endif %}
```

## Running specific models[​](https://docs.getdbt.com/reference/commands/run?version=1.12#running-specific-models "Direct link to Running specific models")
dbt will also allow you select which specific models you'd like to materialize. This can be useful during special scenarios where you may prefer running a different set of models at various intervals. This can also be helpful when you may want to limit the tables materialized while you develop and test new models.
For more information, see the [Model Selection Syntax Documentation](https://docs.getdbt.com/reference/node-selection/syntax).
For more information on running parents or children of specific models, see the [Graph Operators Documentation](https://docs.getdbt.com/reference/node-selection/graph-operators).
## Treat warnings as errors[​](https://docs.getdbt.com/reference/commands/run?version=1.12#treat-warnings-as-errors "Direct link to Treat warnings as errors")
See [global configs](https://docs.getdbt.com/reference/global-configs/warnings)
## Failing fast[​](https://docs.getdbt.com/reference/commands/run?version=1.12#failing-fast "Direct link to Failing fast")
See [global configs](https://docs.getdbt.com/reference/global-configs/failing-fast)
## Enable or Disable Colorized Logs[​](https://docs.getdbt.com/reference/commands/run?version=1.12#enable-or-disable-colorized-logs "Direct link to Enable or Disable Colorized Logs")
See [global configs](https://docs.getdbt.com/reference/global-configs/print-output#print-color)
## The `--empty` flag[​](https://docs.getdbt.com/reference/commands/run?version=1.12#the---empty-flag "Direct link to the---empty-flag")
The `run` command supports the `--empty` flag for building schema-only dry runs. The `--empty` flag limits the refs and sources to zero rows. dbt will still execute the model SQL against the target data warehouse but will avoid expensive reads of input data. This validates dependencies and ensures your models will build properly.
## Status codes[​](https://docs.getdbt.com/reference/commands/run?version=1.12#status-codes "Direct link to Status codes")
When calling the [list_runs api](https://docs.getdbt.com/dbt-cloud/api-v2#/operations/List%20Runs), you will get a status code for each run returned. The available run status codes are as follows:
  * Queued = 1
  * Starting = 2
  * Running = 3
  * Success = 10
  * Error = 20
  * Canceled = 30
  * Skipped = 40


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/run-operation ---

[Skip to main content](https://docs.getdbt.com/reference/commands/run-operation#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Frun-operation+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Frun-operation+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Frun-operation+so+I+can+ask+questions+about+it.)
On this page
### Overview[​](https://docs.getdbt.com/reference/commands/run-operation#overview "Direct link to Overview")
The `dbt run-operation` command is used to invoke a macro. For usage information, consult the docs on [operations](https://docs.getdbt.com/docs/build/hooks-operations#about-operations).
### Usage[​](https://docs.getdbt.com/reference/commands/run-operation#usage "Direct link to Usage")
```
$ dbt run-operation {macro} --args '{args}'  {macro}        Specify the macro to invoke. dbt will call this macro                        with the supplied arguments and then exit  --args ARGS           Supply arguments to the macro. This dictionary will be                        mapped to the keyword arguments defined in the                        selected macro. This argument should be a YAML string,                        eg. '{my_variable: my_value}'
```

### Command line examples[​](https://docs.getdbt.com/reference/commands/run-operation#command-line-examples "Direct link to Command line examples")
Example 1:
`$ dbt run-operation grant_select --args '{role: reporter}'`
Example 2:
`$ dbt run-operation clean_stale_models --args '{days: 7, dry_run: True}'`
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/seed ---

[Skip to main content](https://docs.getdbt.com/reference/commands/seed#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fseed+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fseed+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fseed+so+I+can+ask+questions+about+it.)
On this page
The `dbt seed` command will load `csv` files located in the `seed-paths` directory of your dbt project into your data warehouse.
### Selecting seeds to run[​](https://docs.getdbt.com/reference/commands/seed#selecting-seeds-to-run "Direct link to Selecting seeds to run")
Specific seeds can be run using the `--select` flag to `dbt seed`. Example:
```
$ dbt seed --select "country_codes"Found 2 models, 3 tests, 0 archives, 0 analyses, 53 macros, 0 operations, 2 seed files14:46:15 | Concurrency: 1 threads (target='dev')14:46:15 |14:46:15 | 1 of 1 START seed file analytics.country_codes........................... [RUN]14:46:15 | 1 of 1 OK loaded seed file analytics.country_codes....................... [INSERT 3 in 0.01s]14:46:16 |14:46:16 | Finished running 1 seed in 0.14s.
```

For information about configuring seeds (for example, column types and quoting behavior), see [Seed configurations](https://docs.getdbt.com/reference/seed-configs).
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/show ---

[Skip to main content](https://docs.getdbt.com/reference/commands/show#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fshow+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fshow+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fshow+so+I+can+ask+questions+about+it.)
On this page
Use `dbt show` to:
  * Compile the dbt-SQL definition of a single `model`, `test`, `analysis`, or an arbitrary dbt-SQL query passed `--inline`
    * `dbt show` does not support [Python (dbt-py)](https://docs.getdbt.com/docs/build/python-models) models.
    * Only selecting a single node is supported. [Selector methods](https://docs.getdbt.com/reference/node-selection/methods), [graph operators](https://docs.getdbt.com/reference/node-selection/graph-operators), and other methods that select multiple nodes will not be utilized.
  * Run that query against the data warehouse
  * Preview the results in the terminal


## How it works[​](https://docs.getdbt.com/reference/commands/show#how-it-works "Direct link to How it works")
By default, `dbt show` will display the first 5 rows from the query result. This can be customized by passing the `limit` or the `inline` flags , where `n` is the number of rows to display.
If previewing a model, dbt will always compile and run the compiled query from source. It will not select from the already-materialized database relation, even if you've just run the model. (We may support that in the future; if you're interested, upvote or comment on [dbt-core#7391](https://github.com/dbt-labs/dbt-core/issues/7391).)
####  `limit` flag[​](https://docs.getdbt.com/reference/commands/show#limit-flag "Direct link to limit-flag")
  * The `--limit` flag modifies the underlying SQL and not just the number of rows displayed. By using the `--limit n` flag, it means `n` is the number of rows to display and retrieved from the data warehouse.
  * This means dbt wraps your model's query in a subquery or CTE and applies a SQL `limit n` clause so that your data warehouse only processes and returns that number of rows, making it significantly faster for large datasets.


####  `inline` flag[​](https://docs.getdbt.com/reference/commands/show#inline-flag "Direct link to inline-flag")
  * The results of the preview query are only included in dbt's logs and displayed in the terminal and aren't materialized in the data warehouse or stored in any dbt file, except if you use `dbt show --inline`.
  * The `--inline` flags enables you to run ad-hoc SQL, which means dbt can't ensure the query doesn't modify the data warehouse. To ensure no changes are made, use a profile or role with read-only permissions, which are managed directly in your data warehouse. For example: `dbt show --inline "select * from my_table" --profile my-read-only-profile`.


###  `--output json` flag[​](https://docs.getdbt.com/reference/commands/show#--output-json-flag "Direct link to --output-json-flag")
  * The `--output json` flag returns `dbt show` results in JSON format instead of the default human-readable output, which is helpful for scripting and automation.
  * If you want the full terminal output (including logs) to be machine-readable JSON, you can also set `--log-format json`.


## Example[​](https://docs.getdbt.com/reference/commands/show#example "Direct link to Example")
```
dbt show --select "model_name.sql"
```

or
```
dbt show --inline "select * from {{ ref('model_name') }}"
```

The following is an example of `dbt show` output for a model named `stg_orders`:
```
dbt show --select"stg_orders"21:17:38 Running with dbt=1.5.0-b521:17:38 Found 5 models, 20 tests, 0 snapshots, 0 analyses, 425 macros, 0 operations, 3 seed files, 0 sources, 0 exposures, 0 metrics, 0groups21:17:3821:17:38 Concurrency: 24 threads (target='dev')21:17:3821:17:38 Previewing node'stg_orders':| order_id | customer_id | order_date | status    ||----------+-------------+------------+--------   ||1|1|2023-01-01 | returned  ||2|3|2023-01-02 | completed ||3|94|2023-01-03 | completed ||4|50|2023-01-04 | completed ||5|64|2023-01-05 | completed |
```

For example, if you've just built a model that has a failing test, you can quickly preview the test failures right in the terminal, to find values of `id` that are duplicated:
```
$ dbt build -s"my_model_with_duplicates"13:22:47 .013:22:48 Completed with 1 error and 0 warnings:13:22:4813:22:48 Failure intest unique_my_model_with_duplicates (models/schema.yml)13:22:48   Got 1 result, configured to fail if not 013:22:4813:22:48   compiled code at target/compiled/my_dbt_project/models/schema.yml/unique_my_model_with_duplicates_id.sql13:22:4813:22:48 Done. PASS=1WARN=0ERROR=1SKIP=0TOTAL=2$ dbt show -s"unique_my_model_with_duplicates_id"13:22:53 Running with dbt=1.5.013:22:53 Found 4 models, 2 tests, 0 snapshots, 0 analyses, 309 macros, 0 operations, 0 seed files, 0 sources, 0 exposures, 0 metrics, 0groups13:22:5313:22:53 Concurrency: 5 threads (target='dev')13:22:5313:22:53 Previewing node'unique_my_model_with_duplicates_id':| unique_field | n_records || ------------ | --------- |
```

```
dbt show --inline"select 1"--output json --log-format json
```

Gives you a result like this:
```
"data":{"is_inline":true,"node_name":"inline_query","output_format":"json","preview":"[{\"ID\": 1}]","quiet":false,"unique_id":"sql_operation.jaffle_shop.inline_query""info":{"code":"Q041","level":"info","msg":"{\n  \"show\": [\n    {\n      \"ID\": 1\n    }\n  ]\n}\n","name":"ShowNode","thread":"MainThread"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/test ---

[Skip to main content](https://docs.getdbt.com/reference/commands/test#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Ftest+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Ftest+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Ftest+so+I+can+ask+questions+about+it.)
`dbt test` runs data tests defined on models, sources, snapshots, and seeds and unit tests defined on SQL models. It expects that you have already created those resources through the appropriate commands.
The tests to run can be selected using the `--select` flag discussed [here](https://docs.getdbt.com/reference/node-selection/syntax).
```
# run data and unit testsdbt test# run only data testsdbt test--select test_type:data# run only unit testsdbt test--select test_type:unit# run tests for one_specific_modeldbt test--select"one_specific_model"# run tests for all models in packagedbt test--select"some_package.*"# run only data tests defined singularlydbt test--select"test_type:singular"# run only data tests defined genericallydbt test--select"test_type:generic"# run data tests limited to one_specific_modeldbt test--select"one_specific_model,test_type:data"# run unit tests limited to one_specific_modeldbt test--select"one_specific_model,test_type:unit"
```

For more information on writing tests, read the [data testing](https://docs.getdbt.com/docs/build/data-tests) and [unit testing](https://docs.getdbt.com/docs/build/unit-tests) documentation.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/snapshot ---

[Skip to main content](https://docs.getdbt.com/reference/commands/snapshot#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fsnapshot+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fsnapshot+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fsnapshot+so+I+can+ask+questions+about+it.)
The `dbt snapshot` command executes the [Snapshots](https://docs.getdbt.com/docs/build/snapshots) defined in your project.
dbt will look for Snapshots in the `snapshot-paths` paths defined in your `dbt_project.yml` file. By default, the `snapshot-paths` path is `snapshots/`.
**Usage:**
```
$ dbt snapshot --helpusage: dbt snapshot [-h] [--profiles-dir PROFILES_DIR]                                     [--profile PROFILE] [--target TARGET]                                     [--vars VARS] [--bypass-cache]                                     [--threads THREADS]                                     [--select SELECTOR [SELECTOR ...]]                                     [--exclude EXCLUDE [EXCLUDE ...]]optional arguments:  --select SELECTOR [SELECTOR ...]                        Specify the snapshots to include in the run.  --exclude EXCLUDE [EXCLUDE ...]                        Specify the snapshots to exclude in the run.
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/version ---

[Skip to main content](https://docs.getdbt.com/reference/commands/version#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fversion+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fversion+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fversion+so+I+can+ask+questions+about+it.)
On this page
The `--version` command-line flag returns information about the currently installed version of dbt Core or the dbt CLI. This flag is not supported when invoking dbt in other dbt runtimes (for example, the IDE or scheduled runs).
  * **dbt Core** — Returns the installed version of dbt Core and the versions of all installed adapters.
  * **dbt CLI** — Returns the installed version of the [dbt CLI](https://docs.getdbt.com/docs/cloud/cloud-cli-installation) and, for the other `dbt_version` values, the _latest_ version of the dbt runtime in dbt.


## Versioning[​](https://docs.getdbt.com/reference/commands/version#versioning "Direct link to Versioning")
To learn more about release versioning for dbt Core, refer to [How dbt Core uses semantic versioning](https://docs.getdbt.com/docs/dbt-versions/core#how-dbt-core-uses-semantic-versioning).
If using a [dbt release track](https://docs.getdbt.com/docs/dbt-versions/cloud-release-tracks), which provide ongoing updates to dbt, then `dbt_version` represents the release version of dbt in dbt. This also follows semantic versioning guidelines, using the `YYYY.M.D+<suffix>` format. The year, month, and day represent the date the version was built (for example, `2024.10.8+996c6a8`). The suffix provides an additional unique identification for each build.
## Example usages[​](https://docs.getdbt.com/reference/commands/version#example-usages "Direct link to Example usages")
dbt Core example:
dbt Core
```
$ dbt --versionCore:  - installed: 1.7.6  - latest:    1.7.6 - Up to date!Plugins:  - snowflake: 1.7.1 - Up to date!
```

dbt CLI example:
dbt CLI
```
$ dbt --versionCloud CLI - 0.35.7 (fae78a6f5f6f2d7dff3cab3305fe7f99bd2a36f3 2024-01-18T22:34:52Z)
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/commands/source ---

[Skip to main content](https://docs.getdbt.com/reference/commands/source#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fsource+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fsource+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fcommands%2Fsource+so+I+can+ask+questions+about+it.)
On this page
The `dbt source` command provides subcommands that are useful when working with source data. This command provides one subcommand, `dbt source freshness`.
### dbt source freshness[​](https://docs.getdbt.com/reference/commands/source#dbt-source-freshness "Direct link to dbt source freshness")
If your dbt project is [configured with sources](https://docs.getdbt.com/docs/build/sources), then the `dbt source freshness` command will query all of your defined source tables, determining the "freshness" of these tables. If the tables are stale (based on the `freshness` config specified for your sources) then dbt will report a warning or error accordingly. If a source table is in a stale state, then dbt will exit with a nonzero exit code.
You can also use [source freshness commands](https://docs.getdbt.com/reference/commands/source#source-freshness-commands) to help make sure the data you get is new and not old or outdated.
### Configure source freshness[​](https://docs.getdbt.com/reference/commands/source#configure-source-freshness "Direct link to Configure source freshness")
The example below, shows how to configure source freshness in dbt. Refer to [Declaring source freshness](https://docs.getdbt.com/docs/build/sources#declaring-source-freshness) for more information.
models/<filename>.yml
```
sources:-name: jaffle_shopdatabase: rawconfig:freshness:# changed to config in v1.9warn_after:{count:12,period: hour}error_after:{count:24,period: hour}loaded_at_field: _etl_loaded_at # changed to config in v1.10tables:-name: customers-name: ordersconfig:freshness:warn_after:{count:6,period: hour}error_after:{count:12,period: hour}filter: datediff('day', _etl_loaded_at, current_timestamp) < 2-name: product_skusconfig:freshness:null
```

This helps to monitor the data pipeline health.
You can also configure source freshness in the **Execution settings** section in your dbt job **Settings** page. For more information, refer to [Enabling source freshness snapshots](https://docs.getdbt.com/docs/deploy/source-freshness#enabling-source-freshness-snapshots).
### Source freshness commands[​](https://docs.getdbt.com/reference/commands/source#source-freshness-commands "Direct link to Source freshness commands")
Source freshness commands ensure you're receiving the most up-to-date, relevant, and accurate information.
Some of the typical commands you can use are:
**Command** | **Description**
---|---
[`dbt source freshness`](https://docs.getdbt.com/reference/commands/source#dbt-source-freshness) | Checks the "freshness" for all sources.
[`dbt source freshness --output target/source_freshness.json`](https://docs.getdbt.com/reference/commands/source#configuring-source-freshness-output) | Output of "freshness" information to a different path.
[`dbt source freshness --select "source:source_name"`](https://docs.getdbt.com/reference/commands/source#specifying-sources-to-snapshot) | Checks the "freshness" for specific sources.
Loading table...
---
### Specifying sources to snapshot[​](https://docs.getdbt.com/reference/commands/source#specifying-sources-to-snapshot "Direct link to Specifying sources to snapshot")
By default, `dbt source freshness` will calculate freshness information for all of the sources in your project. To snapshot freshness for a subset of these sources, use the `--select` flag.
```
# Snapshot freshness for all Snowplow tables:$ dbt source freshness --select"source:snowplow"# Snapshot freshness for a particular source table:$ dbt source freshness --select"source:snowplow.event"
```

### Configuring source freshness output[​](https://docs.getdbt.com/reference/commands/source#configuring-source-freshness-output "Direct link to Configuring source freshness output")
When `dbt source freshness` completes, a JSON file containing information about the freshness of your sources will be saved to `target/sources.json`. An example `sources.json` will look like:
target/sources.json
```
"meta":{"generated_at":"2019-02-15T00:53:03.971126Z","elapsed_time":0.21452808380126953"sources":{"source.project_name.source_name.table_name":{"max_loaded_at":"2019-02-15T00:45:13.572836+00:00Z","snapshotted_at":"2019-02-15T00:53:03.880509+00:00Z","max_loaded_at_time_ago_in_s":481.307673,"state":"pass","criteria":{"warn_after":{"count":12,"period":"hour""error_after":{"count":1,"period":"day"
```

To override the destination for this `sources.json` file, use the `-o` (or `--output`) flag:
```
# Output source freshness info to a different path$ dbt source freshness --output target/source_freshness.json
```

### Using source freshness[​](https://docs.getdbt.com/reference/commands/source#using-source-freshness "Direct link to Using source freshness")
Snapshots of source freshness can be used to understand:
  1. If a specific data source is in a delayed state
  2. The trend of data source freshness over time


This command can be run manually to determine the state of your source data freshness at any time. It is also recommended that you run this command on a schedule, storing the results of the freshness snapshot at regular intervals. These longitudinal snapshots will make it possible to be alerted when source data freshness SLAs are violated, as well as understand the trend of freshness over time.
dbt makes it easy to snapshot source freshness on a schedule, and provides a dashboard out of the box indicating the state of freshness for all of the sources defined in your project. For more information on snapshotting freshness in dbt, check out the [docs](https://docs.getdbt.com/docs/build/sources#source-data-freshness).
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12 ---

[Skip to main content](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fabout-database-permissions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fabout-database-permissions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdatabase-permissions%2Fabout-database-permissions+so+I+can+ask+questions+about+it.)
On this page
Database permissions are access rights and privileges granted to users or roles within a database or data platform. They help you specify what actions users or roles can perform on various database objects, like tables, views, schemas, or even the entire database.
### Why are they useful[​](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#why-are-they-useful "Direct link to Why are they useful")
  * Database permissions are essential for security and data access control.
  * They ensure that only authorized users can perform specific actions.
  * They help maintain data integrity, prevent unauthorized changes, and limit exposure to sensitive data.
  * Permissions also support compliance with data privacy regulations and auditing.


### How to use them[​](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#how-to-use-them "Direct link to How to use them")
  * Users and administrators can grant and manage permissions at various levels (such as table, schema, and so on) using SQL statements or through the database system's interface.
  * Assign permissions to individual users or roles (groups of users) based on their responsibilities.
    * Typical permissions include "SELECT" (read), "INSERT" (add data), "UPDATE" (modify data), "DELETE" (remove data), and administrative rights like "CREATE" and "DROP."
  * Users should be assigned permissions that ensure they have the necessary access to perform their tasks without overextending privileges.


Something to note is that each data platform provider might have different approaches and names for privileges. Refer to their documentation for more details.
### Examples[​](https://docs.getdbt.com/reference/database-permissions/about-database-permissions?version=1.12#examples "Direct link to Examples")
Refer to the following database permission pages for more info on examples and how to set up database permissions:


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/data-test-configs ---

[Skip to main content](https://docs.getdbt.com/reference/data-test-configs#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdata-test-configs+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdata-test-configs+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdata-test-configs+so+I+can+ask+questions+about+it.)
On this page
## Related documentation[​](https://docs.getdbt.com/reference/data-test-configs#related-documentation "Direct link to Related documentation")


Data tests can be configured in a few different ways:
  1. Properties within `.yml` definition (generic tests only, see [test properties](https://docs.getdbt.com/reference/resource-properties/data-tests) for full syntax)
  2. A `config()` block within the test's SQL definition
  3. In `dbt_project.yml`


Data test configs are applied hierarchically, in the order of specificity outlined above. In the case of a singular test, the `config()` block within the SQL definition takes precedence over configs in the project YAML file. In the case of a specific instance of a generic test, the test's `.yml` properties would take precedence over any values set in its generic SQL definition's `config()`, which in turn would take precedence over values set in the project YAML file (`dbt_project.yml`).
## Available configurations[​](https://docs.getdbt.com/reference/data-test-configs#available-configurations "Direct link to Available configurations")
Click the link on each configuration option to read more about what it can do.
### Data test-specific configurations[​](https://docs.getdbt.com/reference/data-test-configs#data-test-specific-configurations "Direct link to Data test-specific configurations")
Resource-specific configurations are applicable to only one dbt resource type rather than multiple resource types. You can define these settings in the project file (`dbt_project.yml`), a property file (`models/properties.yml` for models, similarly for other resources), or within the resource’s file using the `{{ config() }}` macro.
The following resource-specific configurations are only available to Data tests:
  * Project file
  * SQL file config
  * Property file


dbt_project.yml
```
data_tests::: <string>: <integer>: error | warn: <string>: <string>: true | false: <string>
```

```
{{ config( = "<string>", = <integer>, = "error | warn", = "<string>", = "<string>", = true | false, = "<string>") }}
```

```
<resource_type>:-name: <resource_namedata_tests:-<test_name>:# # Actual name of the test. For example, dbt_utils.equalityname:# Human friendly name for the test. For example, equality_fct_test_coverage: "markdown formatting"arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.<argument_name>: <argument_value:: <string>: <integer>: error | warn: <string>: <string>: true | false: <string>:-name: <column_namedata_tests:-<test_name>:: "markdown formatting"arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.<argument_name>: <argument_value:: <string>: <integer>: error | warn: <string>: <string>: true | false: <string>
```

This configuration mechanism is supported for specific instances of generic tests only. To configure a specific singular test, you should use the `config()` macro in its SQL definition.
### General configurations[​](https://docs.getdbt.com/reference/data-test-configs#general-configurations "Direct link to General configurations")
General configurations provide broader operational settings applicable across multiple resource types. Like resource-specific configurations, these can also be set in the project file, property files, or within resource-specific files.
  * Project file
  * SQL file config
  * Property file


dbt_project.yml
```
data_tests::: true | false: <string> | [<string>]: {dictionary}    # relevant for  only: <string>: <string>: <string>
```

```
{{ config(=true | false,="<string>" | ["<string>"]={dictionary},="<string>",="<string>",="<string>",) }}
```

```
<resource_type>:-name: <resource_namedata_tests:-<test_name>:# Actual name of the test. For example, dbt_utils.equalityname:# Human friendly name for the test. For example, equality_fct_test_coverage: "markdown formatting"arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.<argument_name>: <argument_value:: true | false: <string> | [<string>]: {dictionary}            # relevant for  only: <string>: <string>: <string>:-name: <column_namedata_tests:-<test_name>:: "markdown formatting"arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.<argument_name>: <argument_value:: true | false: <string> | [<string>]: {dictionary}                # relevant for  only: <string>: <string>: <string>
```

This configuration mechanism is supported for specific instances of generic data tests only. To configure a specific singular test, you should use the `config()` macro in its SQL definition.
### Examples[​](https://docs.getdbt.com/reference/data-test-configs#examples "Direct link to Examples")
#### Add a tag to one test[​](https://docs.getdbt.com/reference/data-test-configs#add-a-tag-to-one-test "Direct link to Add a tag to one test")
If a specific instance of a generic data test:
models/<filename>.yml
```
models:-name: my_modelcolumns:-name: iddata_tests:-unique:config:tags:['my_tag']# changed to config in v1.10
```

If a singular data test:
tests/<filename>.sql
```
{{ config(tags =['my_tag']) }}select...
```

#### Set the default severity for all instances of a generic data test[​](https://docs.getdbt.com/reference/data-test-configs#set-the-default-severity-for-all-instances-of-a-generic-data-test "Direct link to Set the default severity for all instances of a generic data test")
macros/<filename>.sql
```
{% test my_test()%}    {{ config(severity ='warn') }}select...{% endtest %}
```

#### Disable all data tests from a package[​](https://docs.getdbt.com/reference/data-test-configs#disable-all-data-tests-from-a-package "Direct link to Disable all data tests from a package")
dbt_project.yml
```
data_tests:package_name:+enabled:false
```

#### Specify custom configurations for generic data tests[​](https://docs.getdbt.com/reference/data-test-configs#specify-custom-configurations-for-generic-data-tests "Direct link to Specify custom configurations for generic data tests")
Beginning in dbt v1.9, you can use any custom config key to specify custom configurations for data tests. For example, the following specifies the `snowflake_warehouse` custom config that dbt should use when executing the `accepted_values` data test:
```
models:-name: my_modelcolumns:-name: colordata_tests:-accepted_values:arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.values:['blue','red']config:severity: warnsnowflake_warehouse: my_warehouse
```

Given the config, the data test runs on a different Snowflake virtual warehouse than the one in your default connection to enable better price-performance with a different warehouse size or more granular cost allocation and visibility.
#### Add a description to generic and singular tests[​](https://docs.getdbt.com/reference/data-test-configs#add-a-description-to-generic-and-singular-tests "Direct link to Add a description to generic and singular tests")
Starting from dbt v1.9 (also available to dbt [release tracks](https://docs.getdbt.com/docs/dbt-versions/cloud-release-tracks)), you can add [descriptions](https://docs.getdbt.com/reference/resource-properties/data-tests#description) to both generic and singular tests.
For a generic test, add the description in line with the existing YAML:
models/staging/<filename>.yml
```
models:-name: my_modelcolumns:-name: delivery_statusdata_tests:-accepted_values:arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.values:['delivered','pending','failed']description:"This test checks whether there are unexpected delivery statuses. If it fails, check with logistics team"
```

You can also add descriptions to the Jinja macro that provides the core logic of a generic data test. Refer to the [Add description to generic data test logic](https://docs.getdbt.com/best-practices/writing-custom-generic-tests#add-description-to-generic-data-test-logic) for more information.
For a singular test, define it in the test's directory:
tests/my_custom_test.yml
```
data_tests:-name: my_custom_testdescription:"This test checks whether the rolling average of returns is inside of expected bounds. If it isn't, flag to customer success team"
```

For more information refer to [Add a description to a data test](https://docs.getdbt.com/reference/resource-properties/description#add-a-description-to-a-data-test).
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_bool+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_bool+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_bool+so+I+can+ask+questions+about+it.)
On this page
The `as_bool` Jinja filter will coerce Jinja-compiled output into a boolean value (`True` or `False`), or return an error if it cannot be represented as a bool.
### Usage:[​](https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool#usage "Direct link to Usage:")
In the example below, the `as_bool` filter is used to coerce a Jinja expression to enable or disable a set of models based on the `target`.
dbt_project.yml
```
models:my_project:for_export:enabled:"{{ (target.name == 'prod') | as_bool }}"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/adapter ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fadapter+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fadapter+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fadapter+so+I+can+ask+questions+about+it.)
On this page
Your database communicates with dbt using an internal database adapter object. For example, BaseAdapter and SnowflakeAdapter. The Jinja object `adapter` is a wrapper around this internal database adapter object.
`adapter` grants the ability to invoke adapter methods of that internal class via:
  * `{% do adapter.<method name> %}` -- invoke internal adapter method
  * `{{ adapter.<method name> }}` -- invoke internal adapter method and capture its return value for use in materialization or other macros


For example, the adapter methods below will be translated into specific SQL statements depending on the type of adapter your project is using:
  * [adapter.get_missing_columns](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_missing_columns)
  * [adapter.expand_target_column_types](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#expand_target_column_types)
  * [adapter.get_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_relation) or [load_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#load_relation)
  * [adapter.get_columns_in_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_columns_in_relation)
  * [adapter.create_schema](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#create_schema)
  * [adapter.drop_schema](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#drop_schema)
  * [adapter.drop_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#drop_relation)
  * [adapter.rename_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#rename_relation)
  * [adapter.quote](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#quote)


### Deprecated adapter functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#deprecated-adapter-functions "Direct link to Deprecated adapter functions")
The following adapter functions are deprecated, and will be removed in a future release.
  * [adapter.get_columns_in_table](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_columns_in_table) **(deprecated)**
  * [adapter.already_exists](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#already_exists) **(deprecated)**
  * [adapter_macro](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#adapter_macro) **(deprecated)**


## dispatch[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#dispatch "Direct link to dispatch")
Moved to separate page: [dispatch](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch)
## get_missing_columns[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_missing_columns "Direct link to get_missing_columns")
**Args** :
  * `from_relation`: The source [Relation](https://docs.getdbt.com/reference/dbt-classes#relation)
  * `to_relation`: The target [Relation](https://docs.getdbt.com/reference/dbt-classes#relation)


Returns a list of [Columns](https://docs.getdbt.com/reference/dbt-classes#column) that is the difference of the columns in the `from_table` and the columns in the `to_table`, i.e. (`set(from_relation.columns) - set(to_table.columns)`). Useful for detecting new columns in a source table.
**Usage** :
models/example.sql
```
{%-set target_relation = api.Relation.create(database='database_name',schema='schema_name',      identifier='table_name')-%}{%for col in adapter.get_missing_columns(target_relation, this)%}altertable {{this}} addcolumn"{{col.name}}" {{col.data_type}};{% endfor %}
```

## expand_target_column_types[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#expand_target_column_types "Direct link to expand_target_column_types")
**Args** :
  * `from_relation`: The source [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) to use as a template
  * `to_relation`: The [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) to mutate


Expand the `to_relation` table's column types to match the schema of `from_relation`. Column expansion is constrained to string and numeric types on supported databases. Typical usage involves expanding column types (from eg. `varchar(16)` to `varchar(32)`) to support insert statements.
**Usage** :
example.sql
```
{%set tmp_relation = adapter.get_relation(...)%}{%set target_relation = adapter.get_relation(...)%}{%do adapter.expand_target_column_types(tmp_relation, target_relation)%}
```

## get_relation[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_relation "Direct link to get_relation")
**Args** :
  * `database`: The database of the relation to fetch
  * `schema`: The schema of the relation to fetch
  * `identifier`: The identifier of the relation to fetch


Returns a cached [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) object identified by the `database.schema.identifier` provided to the method, or `None` if the relation does not exist.
**Usage** :
example.sql
```
{%-set source_relation = adapter.get_relation(database="analytics",schema="dbt_drew",      identifier="orders")-%}{{ log("Source Relation: "~ source_relation, info=true) }}
```

## load_relation[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#load_relation "Direct link to load_relation")
**Args** :
  * `relation`: The [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) to try to load


A convenience wrapper for [get_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_relation). Returns the cached version of the [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) object, or `None` if the relation does not exist.
**Usage** :
example.sql
```
{%set relation_exists = load_relation(ref('my_model'))isnot none %}{%if relation_exists %}      {{ log("my_model has already been built", info=true) }}{%else%}      {{ log("my_model doesn't exist in the warehouse. Maybe it was dropped?", info=true) }}{% endif %}
```

## get_columns_in_relation[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_columns_in_relation "Direct link to get_columns_in_relation")
**Args** :
  * `relation`: The [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) to find the columns for


Returns a list of [Columns](https://docs.getdbt.com/reference/dbt-classes#column) in a table.
**Usage** :
example.sql
```
{%-setcolumns= adapter.get_columns_in_relation(this)-%}{%forcolumnincolumns%}  {{ log("Column: "~column, info=true) }}{% endfor %}
```

## create_schema[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#create_schema "Direct link to create_schema")
**Args** :
  * `relation`: A relation object with the database and schema to create. Any identifier on the relation will be ignored.


Creates a schema (or equivalent) in the target database. If the target schema already exists, then this method is a no-op.
**Usage:**
example.sql
```
{%do adapter.create_schema(api.Relation.create(database=target.database,schema="my_schema"))%}
```

## drop_schema[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#drop_schema "Direct link to drop_schema")
**Args** :
  * `relation`: A relation object with the database and schema to drop. Any identifier on the relation will be ignored.


Drops a schema (or equivalent) in the target database. If the target schema does not exist, then this method is a no-op. The specific implementation is adapter-dependent, but adapters should implement a cascading drop, such that objects in the schema are also dropped. **Note** : this adapter method is destructive, so please use it with care!
**Usage:**
example.sql
```
{%do adapter.drop_schema(api.Relation.create(database=target.database,schema="my_schema"))%}
```

## drop_relation[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#drop_relation "Direct link to drop_relation")
**Args** :
  * `relation`: The Relation to drop


Drops a Relation in the database. If the target relation does not exist, then this method is a no-op. The specific implementation is adapter-dependent, but adapters should implement a cascading drop, such that bound views downstream of the dropped relation are also dropped. **Note** : this adapter method is destructive, so please use it with care!
The `drop_relation` method will remove the specified relation from dbt's relation cache.
**Usage:**
example.sql
```
{%do adapter.drop_relation(this)%}
```

## rename_relation[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#rename_relation "Direct link to rename_relation")
**Args** :
  * `from_relation`: The Relation to rename
  * `to_relation`: The destination Relation to rename `from_relation` to


Renames a Relation the database. The `rename_relation` method will rename the specified relation in dbt's relation cache.
**Usage:**
example.sql
```
{%-set old_relation = adapter.get_relation(database=this.database,schema=this.schema,      identifier=this.identifier)-%}{%-set backup_relation = adapter.get_relation(database=this.database,schema=this.schema,      identifier=this.identifier ~"__dbt_backup")-%}{%do adapter.rename_relation(old_relation, backup_relation)%}
```

## quote[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#quote "Direct link to quote")
**Args** :
  * `identifier`: A string to quote


Encloses `identifier` in the correct quotes for the adapter when escaping reserved column names etc.
**Usage:**
example.sql
```
select'abc'as {{ adapter.quote('table_name') }},'def'as {{ adapter.quote('group by') }}
```

## get_columns_in_table[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_columns_in_table "Direct link to get_columns_in_table")
This method is deprecated and will be removed in a future release. Please use [get_columns_in_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_columns_in_relation) instead.
**Args** :
  * `schema_name`: The schema to test
  * `table_name`: The table (or view) from which to select columns


Returns a list of [Columns](https://docs.getdbt.com/reference/dbt-classes#column) in a table.
models/example.sql
```
{%set dest_columns = adapter.get_columns_in_table(schema, identifier)%}{%set dest_cols_csv = dest_columns | map(attribute='quoted')|join(', ')%}insertinto {{ this }} ({{ dest_cols_csv }})(select {{ dest_cols_csv }}from {{ref('another_table')}}
```

## already_exists[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#already_exists "Direct link to already_exists")
This method is deprecated and will be removed in a future release. Please use [get_relation](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#get_relation) instead.
**Args** :
  * `schema`: The schema to test
  * `table`: The relation to look for


Returns true if a relation named like `table` exists in schema `schema`, false otherwise.
models/example.sql
```
select * from {{ref('raw_table')}}{% if adapter.already_exists(this.schema, this.name) %}  where id > (select max(id) from {{this}}){% endif %}
```

## adapter_macro[​](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#adapter_macro "Direct link to adapter_macro")
This method is deprecated and will be removed in a future release. Please use [adapter.dispatch](https://docs.getdbt.com/reference/dbt-jinja-functions/adapter#dispatch) instead.
**Usage:**
macros/concat.sql
```
{% macro concat(fields)-%}  {{ adapter_macro('concat',fields) }}{%- endmacro %}{% macro default__concat(fields)-%}    concat({{ fields|join(', ') }}){%- endmacro %}{% macro redshift__concat(fields)%}    {{ fields|join(' || ') }}{% endmacro %}{% macro snowflake__concat(fields)%}    {{ fields|join(' || ') }}{% endmacro %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-classes ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-classes?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-classes+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-classes+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-classes+so+I+can+ask+questions+about+it.)
On this page
dbt has a number of classes it uses to represent objects in a data warehouse, parts of a dbt project, and the results of a command.
These classes are often useful when building advanced dbt models and macros.
## Relation[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#relation "Direct link to Relation")
The `Relation` object is used to interpolate schema and table names into SQL code with appropriate quoting. This object should _always_ be used instead of interpolating values with `{{ schema }}.{{ table }}` directly. Quoting of the Relation object can be configured using the [`quoting` config](https://docs.getdbt.com/reference/project-configs/quoting).
### Creating relations[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#creating-relations "Direct link to Creating relations")
A `Relation` can be created by calling the `create` class method on the `Relation` class.
Relation.create
```
classRelation:defcreate(database=None, schema=None, identifier=None,type=None):    database (optional): The name of the database for this relation    schema (optional): The name of the schema (or dataset, if on BigQuery) for this relation    identifier (optional): The name of the identifier for this relation    type (optional): Metadata about this relation, eg: "table", "view", "cte"
```

### Using relations[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#using-relations "Direct link to Using relations")
In addition to `api.Relation.create`, dbt returns a Relation when you use [`ref`](https://docs.getdbt.com/reference/dbt-jinja-functions/ref), [`source`](https://docs.getdbt.com/reference/dbt-jinja-functions/source) or [`this`](https://docs.getdbt.com/reference/dbt-jinja-functions/this).
relation_usage.sql
```
{% set relation = api.Relation.create(schema='snowplow', identifier='events') %}-- Return the `database` for this relation{{ relation.database }}-- Return the `schema` (or dataset) for this relation{{ relation.schema }}-- Return the `identifier` for this relation{{ relation.identifier }}-- Return relation name without the database{{ relation.include(database=false) }}-- Return true if the relation is a table{{ relation.is_table }}-- Return true if the relation is a view{{ relation.is_view }}-- Return true if the relation is a cte{{ relation.is_cte }}
```

## Column[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#column "Direct link to Column")
The `Column` object is used to encode information about a column in a relation.
column.py
```
classColumn(object):def__init__(self, column, dtype, char_size=None, numeric_size=None):      column: The name of the column represented by this object      dtype: The data type of the column (database-specific)      char_size: If dtype is a variable width character type, the size of the column, or else None      numeric_size: If dtype is a fixed precision numeric type, the size of the column, or else None# Example usage:col = Column('name','varchar',255)col.is_string()# Truecol.is_numeric()# Falsecol.is_number()# Falsecol.is_integer()# Falsecol.is_float()# Falsecol.string_type()# character varying(255)col.numeric_type('numeric',12,4)# numeric(12,4)
```

### Column API[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#column-api "Direct link to Column API")
### Properties[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#properties "Direct link to Properties")
  * **char_size** : Returns the maximum size for character varying columns
  * **column** : Returns the name of the column
  * **data_type** : Returns the data type of the column (with size/precision/scale included)
  * **dtype** : Returns the data type of the column (without any size/precision/scale included)
  * **name** : Returns the name of the column (identical to `column`, provided as an alias).
  * **numeric_precision** : Returns the maximum precision for fixed decimal columns
  * **numeric_scale** : Returns the maximum scale for fixed decimal columns
  * **quoted** : Returns the name of the column wrapped in quotes


### Instance methods[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#instance-methods "Direct link to Instance methods")
  * **is_string()** : Returns True if the column is a String type (eg. text, varchar), else False
  * **is_numeric()** : Returns True if the column is a fixed-precision Numeric type (eg. `numeric`), else False
  * **is_number()** : Returns True if the column is a number-y type (eg. `numeric`, `int`, `float`, or similar), else False
  * **is_integer()** : Returns True if the column is an integer (eg. `int`, `bigint`, `serial` or similar), else False
  * **is_float()** : Returns True if the column is a float type (eg. `float`, `float64`, or similar), else False
  * **string_size()** : Returns the width of the column if it is a string type, else, an exception is raised


### Static methods[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#static-methods "Direct link to Static methods")
  * **string_type(size)** : Returns a database-useable representation of the string type (eg. `character varying(255)`)
  * **numeric_type(dtype, precision, scale)** : Returns a database-useable representation of the numeric type (eg. `numeric(12, 4)`)


### Using columns[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#using-columns "Direct link to Using columns")
column_usage.sql
```
-- String column{%- set string_column = api.Column('name', 'varchar', char_size=255) %}-- Return true if the column is a string{{ string_column.is_string() }}-- Return true if the column is a numeric{{ string_column.is_numeric() }}-- Return true if the column is a number{{ string_column.is_number() }}-- Return true if the column is an integer{{ string_column.is_integer() }}-- Return true if the column is a float{{ string_column.is_float() }}-- Numeric column{%- set numeric_column = api.Column('distance_traveled', 'numeric', numeric_precision=12, numeric_scale=4) %}-- Return true if the column is a string{{ numeric_column.is_string() }}-- Return true if the column is a numeric{{ numeric_column.is_numeric() }}-- Return true if the column is a number{{ numeric_column.is_number() }}-- Return true if the column is an integer{{ numeric_column.is_integer() }}-- Return true if the column is a float{{ numeric_column.is_float() }}-- Static methods-- Return the string data type for this database adapter with a given size{{ api.Column.string_type(255) }}-- Return the numeric data type for this database adapter with a given precision and scale{{ api.Column.numeric_type('numeric', 12, 4) }}
```

## BigQuery columns[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#bigquery-columns "Direct link to BigQuery columns")
The `Column` type is overridden as a `BigQueryColumn` in BigQuery dbt projects. This object works the same as the `Column` type described above, with the exception of extra properties and methods:
### Properties[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#properties-1 "Direct link to Properties")
  * **fields** : Returns the list of subfields contained within a field (if the column is a STRUCT)
  * **mode** : Returns the "mode" of the column, eg. `REPEATED`


### Instance methods[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#instance-methods-1 "Direct link to Instance methods")
**flatten()** : Return a flattened list of `BigQueryColumns` in which subfields are expanded into their own columns. For example, this nested field:
```
[{"hits": {"pageviews": 1, "bounces": 0}}]
```

will be expanded to:
```
[{"hits.pageviews": 1, "hits.bounces": 0}]
```

## Result objects[​](https://docs.getdbt.com/reference/dbt-classes?version=1.12#result-objects "Direct link to Result objects")
The execution of a resource in dbt generates a `Result` object. This object contains information about the executed node, timing, status, and metadata returned by the adapter. At the end of an invocation, dbt records these objects in [`run_results.json`](https://docs.getdbt.com/reference/artifacts/run-results-json).
  * `node`: Full object representation of the dbt resource (model, seed, snapshot, test) executed, including its `unique_id`
  * `status`: dbt's interpretation of runtime success, failure, or error
  * `thread_id`: Which thread executed this node? E.g. `Thread-1`
  * `execution_time`: Total time spent executing this node, measured in seconds.
  * `timing`: Array that breaks down execution time into steps (often `compile` + `execute`)
  * `message`: How dbt will report this result on the CLI, based on information returned from the database


  * `adapter_response`: Dictionary of metadata returned from the database, which varies by adapter. For example, success `code`, number of `rows_affected`, total `bytes_processed`, and so on. Not applicable for [data tests](https://docs.getdbt.com/docs/build/data-tests).
    * `rows_affected` returns the number of rows modified by the last statement executed. In cases where the query's row count can't be determined or isn't applicable (such as when creating a view), a [standard value](https://peps.python.org/pep-0249/#rowcount) of `-1` is returned for `rowcount`.


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/as_number ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_number+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_number+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_number+so+I+can+ask+questions+about+it.)
On this page
The `as_number` Jinja filter will coerce Jinja-compiled output into a numeric value (integer or float), or return an error if it cannot be represented as a number.
### Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number?version=1.12#usage "Direct link to Usage")
In the example below, the `as_number` filter is used to coerce an environment variables into a numeric value to dynamically control the connection port.
profiles.yml
```
my_profile:outputs:type: postgresport:"{{ env_var('PGPORT') | as_number }}"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Was this page helpful?](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/as_native ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/as_native?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_native+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_native+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fas_native+so+I+can+ask+questions+about+it.)
The `as_native` Jinja filter will coerce Jinja-compiled output into its Python native representation according to [`ast.literal_eval`](https://docs.python.org/3/library/ast.html#ast.literal_eval). The result can be any Python native type (set, list, tuple, dict, etc).
To render boolean and numeric values, it is recommended to use [`as_bool`](https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool) and [`as_number`](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number) instead.
Unlike `as_bool` and `as_number`, `as_native` will return a rendered value regardless of the input type. Ensure that your inputs match expectations.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/config ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fconfig+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fconfig+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fconfig+so+I+can+ask+questions+about+it.)
On this page
The `config` variable exists to handle end-user configuration for custom materializations`unique_key` can be implemented using the `config` variable in your own materializations.
For example, code in the `incremental` materialization like this:
```
{% materialization incremental, default -%}  {%- set unique_key = config.get('unique_key') -%}
```

is responsible for handling model code that looks like this:
```
  config(    materialized='incremental',    unique_key='id'
```

Review [Model configurations](https://docs.getdbt.com/reference/model-configs) for examples and more information on valid arguments.
## config.get[​](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#configget "Direct link to config.get")
**Args** :
  * `name`: The name of the configuration variable (required)
  * `default`: The default value to use if this configuration is not provided (optional)


The `config.get` function is used to get configurations for a model from the end-user. Configs defined in this way are optional, and a default value can be provided.
There are 3 cases:
  1. The configuration variable exists, it is not `None`
  2. The configuration variable exists, it is `None`
  3. The configuration variable does not exist


`config.get()` doesn't return values from `config.meta`. If a key exists only in `meta`, `config.get()` returns the default value and emits a warning. To access custom configurations stored under `meta`, use [`config.meta_get()`](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#configmeta_get).
Example usage:
```
{% materialization incremental,default-%}-- Example w/ no default. unique_key will be None if the user does not provide this configuration%-set unique_key = config.get('unique_key')-%}-- Example w/ alternate value. Use alternative of 'id' if 'unique_key' config is provided, but it is None%-set unique_key = config.get('unique_key')or'id'-%}-- Example w/ default value. Default to 'id' if the 'unique_key' config does not exist%-set unique_key = config.get('unique_key',default='id')-%}-- For custom configs under `meta`, use config.meta_get()%set my_custom_config = config.meta_get('custom_config_key')%}
```

## config.require[​](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#configrequire "Direct link to config.require")
**Args** :
  * `name`: The name of the configuration variable (required)


The `config.require` function is used to get configurations for a model from the end-user. Configs defined using this function are required, and failure to provide them will result in a compilation error.
`config.require()` doesn't return values from `config.meta`. If a key exists only in `meta`, `config.require()` raises an error and emits a warning. To access required custom configurations stored under `meta`, use [`config.meta_require()`](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#configmeta_require).
Example usage:
```
{% materialization incremental,default-%}%-set unique_key = config.require('unique_key')-%}
```

## config.meta_get[​](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#configmeta_get "Direct link to config.meta_get")
This functionality is available starting in dbt Core v1.10 and in the dbt Fusion engine.
**Args** :
  * `name`: The name of the configuration variable to retrieve from `meta` (required)
  * `default`: The default value to use if this configuration is not provided (optional)


The `config.meta_get` function retrieves custom configurations stored under the `meta` dictionary. Unlike `config.get()`, this function exclusively checks `config.meta` and won't result in a deprecation warning.
Use this function when accessing custom configurations that you've defined under `meta` in your model or resource configuration - it's equivalent to writing `config.get('meta').get()`.
Note that `config.meta_get` is not yet supported in Python models. In the meantime, Python models should continue using `dbt.config.get("meta").get("<key>")` to access custom meta configurations. `dbt.config.get_meta("<key>")` is an alias for `dbt.config.get("meta").get("<key>")`.
Example usage:
```
{% materialization custom_materialization,default-%}-- Retrieve a custom config from meta, returns None if not found%-set custom_setting = config.meta_get('custom_setting')-%}-- Retrieve with a default value%-set custom_setting = config.meta_get('custom_setting',default='default_value')-%}
```

Example model configuration:
```
models:-name: my_modelconfig:custom_setting:"my_value"
```

## config.meta_require[​](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#configmeta_require "Direct link to config.meta_require")
This functionality is available starting in dbt Core v1.10 and in the dbt Fusion engine.
**Args** :
  * `name`: The name of the configuration variable to retrieve from `meta` (required)


The `config.meta_require` function retrieves custom configurations stored under the `meta` dictionary. Unlike `config.require()`, this function exclusively checks `config.meta` and won't result in deprecation warnings. If the configuration is not found, dbt raises a compilation error.
Use this function when you need to ensure a custom configuration exists under `meta`.
Note that `config.meta_require` is not yet supported in Python models.
Example usage:
```
{% materialization custom_materialization,default-%}-- Require a custom config from meta, throws error if not found%-set required_setting = config.meta_require('required_setting')-%}
```

Example model configuration:
```
models:-name: my_modelconfig:required_setting:"my_value"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Was this page helpful?](https://docs.getdbt.com/reference/dbt-jinja-functions/config?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/dbt_version ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt_version#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt_version+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt_version+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt_version+so+I+can+ask+questions+about+it.)
On this page
The `dbt_version` variable returns the installed version of dbt that is currently running. It can be used for debugging or auditing purposes. For details about release versioning, refer to [Versioning](https://docs.getdbt.com/reference/commands/version#versioning).
## Example usages[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt_version#example-usages "Direct link to Example usages")
macros/get_version.sql
```
{% macro get_version()%}%do log("The installed version of dbt is: "~ dbt_version, info=true)%}{% endmacro %}
```

```
$ dbt run-operation get_versionThe installed version of dbt is 1.6.0
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/exceptions ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/exceptions#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fexceptions+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fexceptions+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fexceptions+so+I+can+ask+questions+about+it.)
On this page
The `exceptions` namespace can be used to raise warnings and errors in dbt userspace.
## raise_compiler_error[​](https://docs.getdbt.com/reference/dbt-jinja-functions/exceptions#raise_compiler_error "Direct link to raise_compiler_error")
The `exceptions.raise_compiler_error` method will raise a compiler error with the provided message. This is typically only useful in macros or materializations when invalid arguments are provided by the calling model. Note that throwing an exception will cause a model to fail, so please use this variable with care!
**Example usage** :
exceptions.sql
```
{%if number 0or number 100%}  {{ exceptions.raise_compiler_error("Invalid `number`. Got: "~ number) }}{% endif %}
```

## warn[​](https://docs.getdbt.com/reference/dbt-jinja-functions/exceptions#warn "Direct link to warn")
Use the `exceptions.warn` method to raise a compiler warning with the provided message, but any model will still be successful and be treated as a PASS. By default, warnings will not cause dbt runs to fail. However:
  * If you use the `--warn-error` flag, all warnings will be promoted to errors.
  * To promote only Jinja warnings to errors (and leave other warnings alone), use `--warn-error-options`. For example, `--warn-error-options '{"error": ["JinjaLogWarning"]}'`.


Learn more about [Warnings](https://docs.getdbt.com/reference/global-configs/warnings).
**Example usage** :
warn.sql
```
{%if number 0or number 100%}%do exceptions.warn("Invalid `number`. Got: "~ number)%}{% endif %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-properties-yml-context ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-properties-yml-context#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt-properties-yml-context+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt-properties-yml-context+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt-properties-yml-context+so+I+can+ask+questions+about+it.)
On this page
The following context methods and variables are available when configuring resources in a `properties.yml` file.
**Available context methods:**


**Available context variables:**


### Example configuration[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-properties-yml-context#example-configuration "Direct link to Example configuration")
properties.yml
```
# Configure this model to be materialized as a view# in development and a table in production/CI contextsmodels:-name: dim_customersconfig:materialized:"{{ 'view' if target.name == 'dev' else 'table' }}"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/execute ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/execute#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fexecute+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fexecute+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fexecute+so+I+can+ask+questions+about+it.)
On this page
`execute` is a Jinja variable that returns True when dbt is in "execute" mode.
When you execute a `dbt compile` or `dbt run` command, dbt:
  1. Reads all of the files in your project and generates a [manifest](https://docs.getdbt.com/reference/artifacts/manifest-json) comprised of models, tests, and other graph nodes present in your project. During this phase, dbt uses the [`ref`](https://docs.getdbt.com/reference/dbt-jinja-functions/ref) and [`source`](https://docs.getdbt.com/reference/dbt-jinja-functions/source) statements it finds to generate the DAG for your project. **No SQL is run during this phase** , and `execute == False`.
  2. Compiles (and runs) each node (eg. building models, or running tests). **SQL is run during this phase** , and `execute == True`.


Any Jinja that relies on a result being returned from the database will error during the parse phase. For example, this SQL will return an error:
models/order_payment_methods.sql
```
1%set payment_method_query %}2selectdistinct3   payment_method4from {{ ref('raw_payments') }}5orderby16% endset %}8%set results = run_query(payment_method_query)%}10# Return the first column #}11%set payment_methods = results.columns[0].values()%}
```

The error returned by dbt will look as follows:
```
Encountered an error:Compilation Error in model order_payment_methods (models/order_payment_methods.sql)  'None' has no attribute 'table'
```

This is because line #11 in the earlier code example (`{% set payment_methods = results.columns[0].values() %}`) assumes that a table has been returned, when, during the parse phase, this query hasn't been run.
To work around this, wrap any problematic Jinja in an `{% if execute %}` statement:
models/order_payment_methods.sql
```
{%set payment_method_query %}selectdistinctpayment_methodfrom {{ ref('raw_payments') }}orderby1{% endset %}{%set results = run_query(payment_method_query)%}{%ifexecute%}{# Return the first column #}{%set payment_methods = results.columns[0].values()%}{%else%}{%set payment_methods =[]%}{% endif %}
```

## Parsing vs execution[​](https://docs.getdbt.com/reference/dbt-jinja-functions/execute#parsing-vs-execution "Direct link to Parsing vs execution")
Parsing in Jinja is when dbt:
  * Reads your project files.
  * Identifies [`ref`](https://docs.getdbt.com/reference/dbt-jinja-functions/ref) and [`source`](https://docs.getdbt.com/reference/dbt-jinja-functions/source).
  * Identifies macro definitions.
  * Builds the dependency graph (DAG).


It doesn't run any SQL — `execute == False`.
Execution is when dbt actually runs SQL and builds models — `execute == True`.
During execution, dbt:
  * Renders full Jinja templates into SQL.
  * Resolves all instances of `ref()` and `source()` to their corresponding table or view names.
  * Runs the SQL in your models during commands like ([`dbt run`](https://docs.getdbt.com/reference/commands/run)), ([`dbt test`](https://docs.getdbt.com/reference/commands/test)), [`dbt seed`](/reference/commands/seed, or [`dbt snapshot`](https://docs.getdbt.com/reference/commands/snapshot).
  * Creates or updates tables/views in the warehouse.
  * Applies any materializations (incremental, table, view, ephemeral).


`execute` impacts the values of `ref()` and `source()`, and won't work as expected inside of a [`sql_header`](https://docs.getdbt.com/reference/resource-configs/sql_header#usage).
This is because in the initial parse of the project, dbt identifies every use of `ref()` and `source()` to build the DAG, but doesn’t resolve them to actual database identifiers. Instead, it replaces each with a placeholder value to ensure the SQL compiles cleanly during parsing.
## Examples[​](https://docs.getdbt.com/reference/dbt-jinja-functions/execute#examples "Direct link to Examples")
Macros like [`log()`](https://docs.getdbt.com/reference/dbt-jinja-functions/log) and [`exceptions.warn()`](https://docs.getdbt.com/reference/dbt-jinja-functions/exceptions#warn) are still evaluated at parse time, during dbt's "first-pass" Jinja render to extract `ref`, `source` and `config`. As a result, dbt will also run any logging or warning messages during this process.
Even though nothing is being executed yet, dbt still runs those log lines while parsing. This can be confusing — it looks like dbt is doing something real but it’s just parsing.
```
$ dbt run15:42:01  Running with dbt=1.10.215:42:01  I'm running a query now.  <------ this one is misleading!!!! no query is actually being run15:42:01  Found 1 model, 0 tests, 0 snapshots, 0 macros, 0 operations, 0 seed files, 0 sources, 0 exposures, 0 metrics15:42:0115:42:01  Concurrency: 8 threads (target='dev')15:42:0115:42:01  1 of 1 START table model analytics.my_model .................................. [RUN]15:42:01  I'm running a query now15:42:02  1 of 1 OK created table model analytics.my_model ............................. [OK in 0.36s]
```

### Logging fully-qualified relation names[​](https://docs.getdbt.com/reference/dbt-jinja-functions/execute#logging-fully-qualified-relation-names "Direct link to Logging fully-qualified relation names")
Let's assume you have a relation named `relation` obtained using something like `{% set relation = ref('my_model') %}` or `{% set relation = source('source_name', 'table_name') %}` — this will lead to unexpected or confusing behavior during parsing:
```
{%- if load_relation(relation) is none -%}    {{ log("Relation is missing: " ~ relation, True) }}{% endif %}
```

To prevent this, add the `execute` flag to make sure the check only runs when dbt is actually running the code — not just when it's preparing it.
Use the command `do exceptions.warn` to emit a warning during model execution without failing the run.
```
{%- if execute and load_relation(relation) is none -%}    {% ("Relation is missing: " ~ relation) %}    {{ log("Relation is missing: " ~ relation, info=True) }}{%- endif -%}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/fromjson ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/fromjson#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ffromjson+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ffromjson+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ffromjson+so+I+can+ask+questions+about+it.)
On this page
The `fromjson` context method can be used to deserialize a JSON string into a Python object primitive, eg. a `dict` or `list`.
**Args** :
  * `string`: The JSON string to deserialize (required)
  * `default`: A default value to return if the `string` argument cannot be deserialized (optional)


### Usage:[​](https://docs.getdbt.com/reference/dbt-jinja-functions/fromjson#usage "Direct link to Usage:")
```
{% set my_json_str = '{"abc": 123}' %}{% set my_dict = fromjson(my_json_str) %}{% do log(my_dict['abc']) %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/flags ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/flags#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fflags+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fflags+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fflags+so+I+can+ask+questions+about+it.)
On this page
The `flags` variable contains values of flags provided on the command line.
**Example usage:**
flags.sql
```
{%if flags.FULL_REFRESH %}droptable...{%else%}-- no-op{% endif %}
```

The list of available flags is defined in the [`flags` module](https://github.com/dbt-labs/dbt-core/blob/HEAD/core/dbt/flags.py) within `dbt-core`.
Recommended use cases include:
  * different materialization logic based on "run modes," such as `flags.FULL_REFRESH` and `flags.STORE_FAILURES`
  * running hooks conditionally based on the current command / task type, via `flags.WHICH`


**Note:** It is _not_ recommended to use flags as an input to parse-time configurations, properties, or dependencies (`ref` + `source`). Flags are likely to change in every invocation of dbt, and their parsed values will become stale (and yield incorrect results) in subsequent invocations that have partial parsing enabled. For more details, see [the docs on parsing](https://docs.getdbt.com/reference/parsing).
### invocation_args_dict[​](https://docs.getdbt.com/reference/dbt-jinja-functions/flags#invocation_args_dict "Direct link to invocation_args_dict")
For the full set of information passed from the CLI—subcommand, flags, arguments—you can use `invocation_args_dict`. This is equivalent to the `args` dictionary in [`run_results.json`](https://docs.getdbt.com/reference/artifacts/run-results-json).
models/my_model.sql
```
-- invocation_args_dict:-- {{ invocation_args_dict }}-- dbt_metadata_envs:-- {{ dbt_metadata_envs }}select1as id
```

The `invocation_command` key within `invocation_args_dict` includes the entire subcommand when it compiles:
```
$ DBT_ENV_CUSTOM_ENV_MYVAR=myvalue dbt compile -s my_model12:10:22  Running with dbt=1.6.0-b812:10:22  Registered adapter: postgres=1.6.0-b812:10:22  Found 1 seed, 1 model, 349 macros12:10:2212:10:22  Concurrency: 5 threads (target='dev')12:10:2212:10:22  Compiled node'my_model' is:-- invocation_args_dict:-- {'log_format_file':'debug', 'log_level':'info', 'exclude':(), 'send_anonymous_usage_stats': True, 'which':'compile', 'defer': False, 'output':'text', 'log_format':'default', 'macro_debugging': False, 'populate_cache': True, 'static_parser': True, 'vars':{}, 'warn_error_options': WarnErrorOptions(include=[], exclude=[]), 'quiet': False, 'select':('my_model',), 'indirect_selection':'eager', 'strict_mode': False, 'version_check': False, 'enable_legacy_logger': False, 'log_path':'/Users/jerco/dev/scratch/testy/logs', 'profiles_dir':'/Users/jerco/.dbt', 'invocation_command':'dbt compile -s my_model', 'log_level_file':'debug', 'project_dir':'/Users/jerco/dev/scratch/testy', 'favor_state': False, 'use_colors_file': True, 'write_json': True, 'partial_parse': True, 'printer_width':80, 'print': True, 'cache_selected_only': False, 'use_colors': True, 'introspect': True}-- dbt_metadata_envs:-- {'MYVAR':'myvalue'}select1 as id
```

## flags.WHICH[​](https://docs.getdbt.com/reference/dbt-jinja-functions/flags#flagswhich "Direct link to flags.WHICH")
`flags.WHICH` is a global variable that gets set when you run a dbt command. If used in a macro, it allows you to conditionally change behavior depending on the command currently being executed. For example, conditionally modifying SQL:
```
{% macro conditional_filter(table_name)%}# Add a WHERE clause only during `dbt run`, not during `dbt test` or `dbt compile` #}select*from {{ table_name }}%if flags.WHICH =="run"%}where is_active =true% elif flags.WHICH =="test"%}-- In test runs, restrict rows to keep tests fastlimit10% elif flags.WHICH =="compile"%}-- During compile, just add a harmless comment-- compile mode detected% endif %}{% endmacro %}
```

The following commands are supported:
`flags.WHICH` value | Description
---|---
`"build"` | Build and test all selected resources.
`"clean"` | Remove artifacts like target directory and packages.
`"clone"` | Clone models and other resources.
`"compile"` | Compile SQL, but do not execute.
`"debug"` | Test connections and validate configs.
`"deps"` | Download package dependencies.
`"docs"` | Generate and serve documentation.
`"environment"` | Workspace environment commands (cloud CLI).
`"help"` | Show help for commands and subcommands.
`"init"` | Bootstrap a new project.
`"invocation"` | For interacting with or inspecting current invocation (cloud CLI).
`"list"` | List resources.
`"parse"` | Parse project and report errors, but don’t build/test.
`"retry"` | Retry the last invocation from the point of failure.
`"run"` | Execute models.
`"run-operation"` | Invoke arbitrary macros or SQL ops.
`"seed"` | Load CSV(s) into the database.
`"show"` | Inspect resource definitions or materializations.
`"snapshot"` | Execute snapshots.
`"source"` | Validate freshness and inspect source definitions.
`"test"` | Schema and data tests.
`"version"` | Display dbt version.
Loading table...
---
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/env_var ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fenv_var+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fenv_var+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fenv_var+so+I+can+ask+questions+about+it.)
On this page
The `env_var` function can be used to incorporate environment variables from the system into your dbt project. You can use the `env_var` function in your `profiles.yml` file, the `dbt_project.yml` file, the `sources.yml` file, your `schema.yml` files, and in model `.sql` files. Essentially, `env_var` is available anywhere dbt processes Jinja code.
When used in a `profiles.yml` file (to avoid putting credentials on a server), it can be used like this:
profiles.yml
```
profile:target: prodoutputs:type: postgreshost: 127.0.0.1# IMPORTANT: Make sure to quote the entire Jinja string hereuser:"{{ env_var('DBT_USER') }}"password:"{{ env_var('DBT_PASSWORD') }}"
```

If the `DBT_USER` and `DBT_ENV_SECRET_PASSWORD` environment variables are present when dbt is invoked, then these variables will be pulled into the profile as expected. If any environment variables are not set, then dbt will raise a compilation error.
### Converting env_vars[​](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var#converting-env_vars "Direct link to Converting env_vars")
Environment variables are always strings. When using them for configurations that expect integers or booleans, you must explicitly convert the value to the correct type.
Use a Jinja filter to convert the string to the correct type:
  * **Integers** — Convert the string to a number using the `int` or [`as_number`](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number) filter to avoid errors like `'1' is not of type 'integer'`. For example, `"{{ env_var('DBT_THREADS') | int }}"` or `"{{ env_var('DB_PORT') | as_number }}"`.
  * **Booleans** — Convert the string to a boolean explicitly using the [`as_bool`](https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool) filter. For example, `"{{ env_var('DBT_PERSIST_DOCS_RELATION', False) | as_bool }}"`.


For boolean defaults, use capitalized `True` or `False`. Using lowercase `true` or `false` will be treated as a string and can result in unexpected results.
For example, to disable [`persist_docs`](https://docs.getdbt.com/reference/resource-configs/persist_docs) using environment variables:
dbt_project.yml
```
+persist_docs:relation:"{{ env_var('DBT_PERSIST_DOCS_RELATION', False) | as_bool }}"columns:"{{ env_var('DBT_PERSIST_DOCS_COLUMNS', False) | as_bool }}"
```

Be sure to quote the entire Jinja string. Otherwise, the YAML parser will be confused by the Jinja curly brackets.
### Default values[​](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var#default-values "Direct link to Default values")
You can also provide a default value as a second argument:
dbt_project.yml
```
models:jaffle_shop:+materialized:"{{ env_var('DBT_MATERIALIZATION', 'view') }}"
```

This can be useful to avoid compilation errors when the environment variable isn't available.
### Secrets[​](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var#secrets "Direct link to Secrets")
For certain configurations, you can use "secret" env vars. Any env var named with the prefix `DBT_ENV_SECRET` will be:
  * Available for use in `profiles.yml` + `packages.yml`, via the same `env_var()` function
  * Disallowed everywhere else, including `dbt_project.yml` and model SQL, to prevent accidentally writing these secret values to the data warehouse or metadata artifacts
  * Scrubbed from dbt logs and replaced with `*****`, any time its value appears in those logs (even if the env var was not called directly)


The primary use case of secret env vars is git access tokens for [private packages](https://docs.getdbt.com/docs/build/packages#private-packages).
**Note:** When dbt is loading profile credentials and package configuration, secret env vars will be replaced with the string value of the environment variable. You cannot modify secrets using Jinja filters, including type-casting filters such as [`as_number`](https://docs.getdbt.com/reference/dbt-jinja-functions/as_number) or [`as_bool`](https://docs.getdbt.com/reference/dbt-jinja-functions/as_bool), or pass them as arguments into other Jinja macros. You can only use _one secret_ per configuration:
```
# workshost:"{{ env_var('DBT_ENV_SECRET_HOST') }}"# does not workhost:"www.{{ env_var('DBT_ENV_SECRET_HOST_DOMAIN') }}.com/{{ env_var('DBT_ENV_SECRET_HOST_PATH') }}"
```

### Custom metadata[​](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var#custom-metadata "Direct link to Custom metadata")
Any env var named with the prefix `DBT_ENV_CUSTOM_ENV_` will be included in two places, with its prefix-stripped name as the key:
  * [dbt artifacts](https://docs.getdbt.com/reference/artifacts/dbt-artifacts#common-metadata): `metadata` -> `env`
  * [events and structured logs](https://docs.getdbt.com/reference/events-logging#info-fields): `info` -> `extra`


A dictionary of these prefixed env vars will also be available in a `dbt_metadata_envs` context variable:
```
-- {{ dbt_metadata_envs }}select1as id
```

```
$ DBT_ENV_CUSTOM_ENV_MY_FAVORITE_COLOR=indigo DBT_ENV_CUSTOM_ENV_MY_FAVORITE_NUMBER=6 dbt compile
```

Compiles to:
```
-- {'MY_FAVORITE_COLOR': 'indigo', 'MY_FAVORITE_NUMBER': '6'}select1as id
```

### dbt platform usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var#dbt-platform-usage "Direct link to dbt platform usage")
If you are using dbt, you must adhere to the naming conventions for environment variables. Environment variables in dbt must be prefixed with `DBT_` (including `DBT_ENV_CUSTOM_ENV_` or `DBT_ENV_SECRET`). Environment variables keys are uppercased and case sensitive. When referencing `{{env_var('DBT_KEY')}}` in your project's code, the key must match exactly the variable defined in dbt's UI.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/debug-method ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/debug-method#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdebug-method+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdebug-method+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdebug-method+so+I+can+ask+questions+about+it.)
On this page
The `debug()` macro is only available when using dbt Core CLI in a local development environment. It's _not available_ in dbt platform.
Do not deploy code to production that uses the `debug` macro.
If developing in dbt platform or using Fusion, you can instead use:
  * [`{{ print() }}`](https://docs.getdbt.com/reference/dbt-jinja-functions/print) - Print messages to both the log file and standard output (`stdout`).
  * [`{{ log() }}`](https://docs.getdbt.com/reference/dbt-jinja-functions/log) - Structured logging that prints messages during Jinja rendering.


The `{{ debug() }}` macro will open an iPython debugger in the context of a compiled dbt macro. The `DBT_MACRO_DEBUGGING` environment variable must be set to use the debugger.
This function requires:
  * Interactive terminal access with iPython debugger (`ipdb`) installed. Fusion doesn't provide a iPython (ipdb) debugger since its built on Rust. It instead outputs a non-interactive snapshot of the MiniJinja render context in the compiled code.
  * Local development environment running dbt Core CLI
  * `DBT_MACRO_DEBUGGING` environment variable set


## Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/debug-method#usage "Direct link to Usage")
my_macro.sql
```
{% macro my_macro() %}  {% set something_complex = my_complicated_macro() %}  {{ debug() }}{% endmacro %}
```

When dbt hits the `debug()` line, you'll see something like:
```
$ DBT_MACRO_DEBUGGING=write dbt compileRunning with dbt=1.0 /var/folders/31/mrzqbbtd3rn4hmgbhrtkfyxm0000gn/T/dbt-macro-compiled-cxvhhgu7.py(14)root()13         environment.call(context, (undefined(name='debug')if l_0_debug is missing else l_0_debug)),---14         environment.call(context, (undefined(name='source')if l_0_source is missing else l_0_source), 'src', 'seedtable'),ipdb9,129     l_0_debug = resolve('debug')10     l_0_source = resolve('source')11     pass12     yield '%s\nselect * from %s'(
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/fromyaml ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/fromyaml#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ffromyaml+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ffromyaml+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ffromyaml+so+I+can+ask+questions+about+it.)
On this page
The `fromyaml` context method can be used to deserialize a YAML string into a Python object primitive, eg. a `dict` or `list`.
**Args** :
  * `string`: The YAML string to deserialize (required)
  * `default`: A default value to return if the `string` argument cannot be deserialized (optional)


### Usage:[​](https://docs.getdbt.com/reference/dbt-jinja-functions/fromyaml#usage "Direct link to Usage:")
```
{% set my_yml_str -%}dogs: - good - bad{%- endset %}{% set my_dict = fromyaml(my_yml_str) %}{% do log(my_dict['dogs'], info=true) %}-- ["good", "bad"]{% do my_dict['dogs'].pop() %}{% do log(my_dict['dogs'], info=true) %}-- ["good"]
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-project-yml-context ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-project-yml-context#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt-project-yml-context+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt-project-yml-context+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdbt-project-yml-context+so+I+can+ask+questions+about+it.)
On this page
The following context methods and variables are available when configuring resources in the `dbt_project.yml` file. This applies to the `models:`, `seeds:`, and `snapshots:` keys in the `dbt_project.yml` file.
**Available context methods:**


**Available context variables:**


### Example configuration[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dbt-project-yml-context#example-configuration "Direct link to Example configuration")
dbt_project.yml
```
name: my_projectversion: 1.0.0# Configure the models in models/facts/ to be materialized as views# in development and tables in production/CI contextsmodels:my_project:facts:+materialized:"{{ 'view' if target.name == 'dev' else 'table' }}"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fcross-database-macros+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fcross-database-macros+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fcross-database-macros+so+I+can+ask+questions+about+it.)
On this page
These macros benefit three different user groups:
  * If you maintain a package, your package is more likely to work on other adapters by using these macros (rather than a specific database's SQL syntax)
  * If you maintain an adapter, your adapter is more likely to support more packages by implementing (and testing) these macros.
  * If you're an end user, more packages and adapters are likely to "just work" for you (without you having to do anything).


Please make sure to take a look at the [SQL expressions section](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions) to understand quoting syntax for string values and date literals.
## All functions (alphabetical)[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#all-functions-alphabetical "Direct link to All functions \(alphabetical\)")
  * [Cross-database macros](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cross-database-macros)
    * [All functions (alphabetical)](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#all-functions-alphabetical)
    * [Data type functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#data-type-functions)
      * [type_timestamp](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_timestamp)
      * [current_timestamp](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#current_timestamp)
    * [Set functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#set-functions)
    * [Array functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array-functions)
      * [array_construct](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array_construct)
    * [String functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string-functions)
    * [String literal functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string-literal-functions)
      * [escape_single_quotes](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#escape_single_quotes)
      * [string_literal](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string_literal)
    * [Aggregate and window functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#aggregate-and-window-functions)
    * [Cast functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast-functions)
      * [cast_bool_to_text](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast_bool_to_text)
    * [Date and time functions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-functions)
    * [Date and time parts](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts)
    * [SQL expressions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions)


[**Data type functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#data-type-functions)
  * [type_timestamp](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_timestamp)


[**Set functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#set-functions)


[**Array functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array-functions)
  * [array_construct](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array_construct)


[**String functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string-functions)


[**String literal functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string-literal-functions)
  * [escape_single_quotes](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#escape_single_quotes)
  * [string_literal](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string_literal)


[**Aggregate and window functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#aggregate-and-window-functions)


[**Cast functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast-functions)
  * [cast_bool_to_text](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast_bool_to_text)


[**Date and time functions**](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-functions)


## Data type functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#data-type-functions "Direct link to Data type functions")
### type_bigint[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_bigint "Direct link to type_bigint")
**Args** :
  * None


This macro yields the database-specific data type for a `BIGINT`.
**Usage** :
```
{{ dbt.type_bigint() }}
```

**Sample Output (PostgreSQL)** :
```
bigint
```

### type_boolean[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_boolean "Direct link to type_boolean")
**Args** :
  * None


This macro yields the database-specific data type for a `BOOLEAN`.
**Usage** :
```
{{ dbt.type_boolean() }}
```

**Sample Output (PostgreSQL)** :
```
BOOLEAN
```

### type_float[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_float "Direct link to type_float")
**Args** :
  * None


This macro yields the database-specific data type for a `FLOAT`.
**Usage** :
```
{{ dbt.type_float() }}
```

**Sample Output (PostgreSQL)** :
```
FLOAT
```

### type_int[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_int "Direct link to type_int")
**Args** :
  * None


This macro yields the database-specific data type for an `INT`.
**Usage** :
```
{{ dbt.type_int() }}
```

**Sample Output (PostgreSQL)** :
### type_numeric[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_numeric "Direct link to type_numeric")
**Args** :
  * None


This macro yields the database-specific data type for a `NUMERIC`.
**Usage** :
```
{{ dbt.type_numeric() }}
```

**Sample Output (PostgreSQL)** :
```
numeric(28,6)
```

### type_string[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_string "Direct link to type_string")
**Args** :
  * None


This macro yields the database-specific data type for `TEXT`.
**Usage** :
```
{{ dbt.type_string() }}
```

**Sample Output (PostgreSQL)** :
```
TEXT
```

### type_timestamp[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#type_timestamp "Direct link to type_timestamp")
**Args** :
  * None


This macro yields the database-specific data type for a `TIMESTAMP` (which may or may not match the behavior of `TIMESTAMP WITHOUT TIMEZONE` from ANSI SQL-92).
**Usage** :
```
{{ dbt.type_timestamp() }}
```

**Sample Output (PostgreSQL)** :
```
TIMESTAMP
```

### current_timestamp[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#current_timestamp "Direct link to current_timestamp")
This macro returns the current date and time for the system. Depending on the adapter:
  * The result may be an aware or naive timestamp.
  * The result may correspond to the start of the statement or the start of the transaction.


**Args**
  * None


**Usage**
  * You can use the `current_timestamp()` macro within your dbt SQL files like this:


```
{{ dbt.current_timestamp() }}
```

**Sample output (PostgreSQL)**
```

```

## Set functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#set-functions "Direct link to Set functions")
### except[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#except "Direct link to except")
**Args** :
  * None


`except` is one of the set operators specified ANSI SQL-92 (along with `union` and `intersect`) and is akin to [set difference](https://en.wikipedia.org/wiki/Complement_\(set_theory\)#Relative_complement).
**Usage** :
```
{{ dbt.except() }}
```

**Sample Output (PostgreSQL)** :
```
except
```

### intersect[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#intersect "Direct link to intersect")
**Args** :
  * None


`intersect` is one of the set operators specified ANSI SQL-92 (along with `union` and `except`) and is akin to [set intersection](https://en.wikipedia.org/wiki/Intersection_\(set_theory\)).
**Usage** :
```
{{ dbt.intersect() }}
```

**Sample Output (PostgreSQL)** :
```
intersect
```

## Array functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array-functions "Direct link to Array functions")
### array_append[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array_append "Direct link to array_append")
**Args** :
  * `array` (required): The array to append to.
  * `new_element` (required): The element to be appended. This element must _match the data type of the existing elements_ in the array in order to match PostgreSQL functionality and _not null_ to match BigQuery functionality.


This macro appends an element to the end of an array and returns the appended array.
**Usage** :
```
{{ dbt.array_append("array_column","element_column") }}{{ dbt.array_append("array_column","5") }}{{ dbt.array_append("array_column","'blue'") }}
```

**Sample Output (PostgreSQL)** :
```
array_append(array_column, element_column)array_append(array_column,5)array_append(array_column,'blue')
```

### array_concat[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array_concat "Direct link to array_concat")
**Args** :
  * `array_1` (required): The array to append to.
  * `array_2` (required): The array to be appended to `array_1`. This array must match the data type of `array_1` in order to match PostgreSQL functionality.


This macro returns the concatenation of two arrays.
**Usage** :
```
{{ dbt.array_concat("array_column_1","array_column_2") }}
```

**Sample Output (PostgreSQL)** :
```
array_cat(array_column_1, array_column_2)
```

### array_construct[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#array_construct "Direct link to array_construct")
**Args** :
  * `inputs` (optional): The list of array contents. If not provided, this macro will create an empty array. All inputs must be the _same data type_ in order to match PostgreSQL functionality and _not null_ to match BigQuery functionality.
  * `data_type` (optional): Specifies the data type of the constructed array. This is only relevant when creating an empty array (will otherwise use the data type of the inputs). If `inputs` are `data_type` are both not provided, this macro will create an empty array of type integer.


This macro returns an array constructed from a set of inputs.
**Usage** :
```
{{ dbt.array_construct(["column_1","column_2","column_3"]) }}{{ dbt.array_construct([],"integer") }}{{ dbt.array_construct([1,2,3,4]) }}{{ dbt.array_construct(["'blue'","'green'"]) }}
```

**Sample Output (PostgreSQL)** :
```
array[ column_1 , column_2 , column_3 ]array[]::integer[]array[1,2,3,4]array['blue','green']
```

## String functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string-functions "Direct link to String functions")
### concat[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#concat "Direct link to concat")
**Args** :
  * `fields`: Jinja array of [attribute names or expressions](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro combines a list of strings together.
**Usage** :
```
{{ dbt.concat(["column_1","column_2"]) }}{{ dbt.concat(["year_column","'-'","month_column","'-'","day_column"]) }}{{ dbt.concat(["first_part_column","'.'","second_part_column"]) }}{{ dbt.concat(["first_part_column","','","second_part_column"]) }}
```

**Sample Output (PostgreSQL)** :
```
column_1 || column_2year_column ||'-'|| month_column ||'-'|| day_columnfirst_part_column ||'.'|| second_part_columnfirst_part_column ||','|| second_part_column
```

### hash[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#hash "Direct link to hash")
**Args** :
  * `field`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro provides a hash (such as [MD5](https://en.wikipedia.org/wiki/MD5)) of an [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions) cast as a string.
**Usage** :
```
{{ dbt.hash("column") }}{{ dbt.hash("'Pennsylvania'") }}
```

**Sample Output (PostgreSQL)** :
```
md5(cast(columnasvarcharmd5(cast('Pennsylvania'asvarchar
```

### length[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#length "Direct link to length")
**Args** :
  * `expression`: string [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro calculates the number of characters in a string.
**Usage** :
```
{{ dbt.length("column") }}
```

**Sample Output (PostgreSQL)** :
```
    length(column
```

### position[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#position "Direct link to position")
**Args** :
  * `substring_text`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `string_text`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro searches for the first occurrence of `substring_text` within `string_text` and returns the 1-based position if found.
**Usage** :
```
{{ dbt.position("substring_column","text_column") }}{{ dbt.position("'-'","text_column") }}
```

**Sample Output (PostgreSQL)** :
```
    position(        substring_column in text_column    position('-'in text_column
```

### replace[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#replace "Direct link to replace")
**Args** :
  * `field`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `old_chars`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `new_chars`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro updates a string and replaces all occurrences of one substring with another. The precise behavior may vary slightly from one adapter to another.
**Usage** :
```
{{ dbt.replace("string_text_column","old_chars_column","new_chars_column") }}{{ dbt.replace("string_text_column","'-'","'_'") }}
```

**Sample Output (PostgreSQL)** :
```
replace(        string_text_column,        old_chars_column,        new_chars_columnreplace(        string_text_column,
```

### right[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#right "Direct link to right")
**Args** :
  * `string_text`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `length_expression`: numeric [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro returns the N rightmost characters from a string.
**Usage** :
```
{{ dbt.right("string_text_column","length_column") }}{{ dbt.right("string_text_column","3") }}
```

**Sample Output (PostgreSQL)** :
```
right(        string_text_column,        length_columnright(        string_text_column,
```

### split_part[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#split_part "Direct link to split_part")
**Args** :
  * `string_text` (required): Text to be split into parts.
  * `delimiter_text` (required): Text representing the delimiter to split by.
  * `part_number` (required): Requested part of the split (1-based). If the value is negative, the parts are counted backward from the end of the string.


This macro splits a string of text using the supplied delimiter and returns the supplied part number (1-indexed).
**Usage** :
When referencing a column, use one pair of quotes. When referencing a string, use single quotes enclosed in double quotes.
```
{{ dbt.split_part(string_text='column_to_split', delimiter_text='delimiter_column', part_number=1) }}{{ dbt.split_part(string_text="'1|2|3'", delimiter_text="'|'", part_number=1) }}
```

**Sample Output (PostgreSQL)** :
```
    split_part(        column_to_split,        delimiter_column,    split_part('1|2|3',
```

## String literal functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string-literal-functions "Direct link to String literal functions")
### escape_single_quotes[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#escape_single_quotes "Direct link to escape_single_quotes")
**Args** :
  * `value`: Jinja string literal value


This macro adds escape characters for any single quotes within the provided string literal. Note: if given a column, it will only operate on the column _name_ , not the values within the column.
To escape quotes for column values, consider a macro like [replace](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#replace) or a regular expression replace.
**Usage** :
```
{{ dbt.escape_single_quotes("they're") }}{{ dbt.escape_single_quotes("ain't ain't a word") }}
```

**Sample Output (PostgreSQL)** :
```
they''reain''t ain''t a word
```

### string_literal[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#string_literal "Direct link to string_literal")
**Args** :
  * `value`: Jinja string value


This macro converts a Jinja string into a SQL string literal.
To cast column values to a string, consider a macro like [safe_cast](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#safe_cast) or an ordinary cast.
**Usage** :
```
select {{ dbt.string_literal("Pennsylvania") }}
```

**Sample Output (PostgreSQL)** :
```
select'Pennsylvania'
```

## Aggregate and window functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#aggregate-and-window-functions "Direct link to Aggregate and window functions")
### any_value[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#any_value "Direct link to any_value")
**Args** :
  * `expression`: an [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro returns some value of the expression from the group. The selected value is non-deterministic (rather than random).
**Usage** :
```
{{ dbt.any_value("column_name") }}
```

**Sample Output (PostgreSQL)** :
```
any(column_name)
```

### bool_or[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#bool_or "Direct link to bool_or")
**Args** :
  * `expression`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro returns the logical `OR` of all non-`NULL` expressions -- `true` if at least one record in the group evaluates to `true`.
**Usage** :
```
{{ dbt.bool_or("boolean_column") }}{{ dbt.bool_or("integer_column = 3") }}{{ dbt.bool_or("string_column = 'Pennsylvania'") }}{{ dbt.bool_or("column1 = column2") }}
```

**Sample Output (PostgreSQL)** :
```
bool_or(boolean_column)bool_or(integer_column =3)bool_or(string_column ='Pennsylvania')bool_or(column1 = column2)
```

### listagg[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#listagg "Direct link to listagg")
**Args** :
  * `measure` (required): The [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions) that determines the values to be concatenated. To only include distinct values add keyword `DISTINCT` to beginning of expression (example: 'DISTINCT column_to_agg').
  * `delimiter_text` (required): Text representing the delimiter to separate concatenated values by.
  * `order_by_clause` (optional): An expression (typically one or more column names separated by commas) that determines the order of the concatenated values.
  * `limit_num` (optional): Specifies the maximum number of values to be concatenated.


This macro returns the concatenated input values from a group of rows separated by a specified delimiter.
**Usage** :
Note: If there are instances of `delimiter_text` within your `measure`, you cannot include a `limit_num`.
```
{{ dbt.listagg(measure="column_to_agg", delimiter_text="','", order_by_clause="order by order_by_column", limit_num=10) }}
```

**Sample Output (PostgreSQL)** :
```
array_to_string((array_agg(            column_to_aggorderby order_by_column))[1:10],
```

## Cast functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast-functions "Direct link to Cast functions")
### cast[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast "Direct link to cast")
**Availability** : dbt v1.8 or higher. For more information, select the version from the documentation navigation menu.
**Args** :
  * `field`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `type`: data type to convert to


This macro casts a value to the specified data type. Unlike [safe_cast](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#safe_cast), this macro will raise an error when the cast fails.
**Usage** :
```
{{ dbt.cast("column_1", api.Column.translate_type("string")) }}{{ dbt.cast("column_2", api.Column.translate_type("integer")) }}{{ dbt.cast("'2016-03-09'", api.Column.translate_type("date")) }}
```

**Sample Output (PostgreSQL)** :
```
    cast(column_1 asTEXT)    cast(column_2 asINT)    cast('2016-03-09'asdate)
```

### cast_bool_to_text[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#cast_bool_to_text "Direct link to cast_bool_to_text")
**Args** :
  * `field`: boolean [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro casts a boolean value to a string.
**Usage** :
```
{{ dbt.cast_bool_to_text("boolean_column_name") }}{{ dbt.cast_bool_to_text("false") }}{{ dbt.cast_bool_to_text("true") }}{{ dbt.cast_bool_to_text("0 = 1") }}{{ dbt.cast_bool_to_text("1 = 1") }}{{ dbt.cast_bool_to_text("null") }}
```

**Sample Output (PostgreSQL)** :
```
    cast(boolean_column_name asvarchar    cast(falseasvarchar    cast(trueasvarchar    cast(0=1asvarchar    cast(1=1asvarchar    cast(nullasvarchar
```

### safe_cast[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#safe_cast "Direct link to safe_cast")
**Args** :
  * `field`: [attribute name or expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `type`: data type to convert to


For databases that support it, this macro will return `NULL` when the cast fails (instead of raising an error).
**Usage** :
```
{{ dbt.safe_cast("column_1", api.Column.translate_type("string")) }}{{ dbt.safe_cast("column_2", api.Column.translate_type("integer")) }}{{ dbt.safe_cast("'2016-03-09'", api.Column.translate_type("date")) }}
```

**Sample Output (PostgreSQL)** :
```
    cast(column_1 asTEXT)    cast(column_2 asINT)    cast('2016-03-09'asdate)
```

## Date and time functions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-functions "Direct link to Date and time functions")
### date[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date "Direct link to date")
**Availability** : dbt v1.8 or later. For more information, select the version from the documentation navigation menu.
**Args** :
  * `year`: an integer
  * `month`: an integer
  * `day`: an integer


This macro converts the `year`, `month`, and `day` into an SQL `DATE` type.
**Usage** :
```
{{ dbt.date(2023,10,4) }}
```

**Sample output (PostgreSQL)** :
```
to_date('2023-10-04','YYYY-MM-DD')
```

### dateadd[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#dateadd "Direct link to dateadd")
**Args** :
  * `datepart`: [date or time part](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts).
  * `interval`: integer count of the `datepart` to add (can be positive or negative)
  * `from_date_or_timestamp`: date/time [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro adds a time/day interval to the supplied date/timestamp. Note: The `datepart` argument is database-specific.
**Usage** :
```
{{ dbt.dateadd(datepart="day",interval=1, from_date_or_timestamp="'2016-03-09'") }}{{ dbt.dateadd(datepart="month",interval=-2, from_date_or_timestamp="'2016-03-09'") }}
```

**Sample Output (PostgreSQL)** :
```
'2016-03-09'+((interval'10 day')*(1))'2016-03-09'+((interval'10 month')*(-2))
```

### datediff[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#datediff "Direct link to datediff")
**Args** :
  * `first_date`: date/time [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `second_date`: date/time [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `datepart`: [date or time part](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts).


This macro calculates the difference between two dates.
**Usage** :
```
{{ dbt.datediff("column_1","column_2","day") }}{{ dbt.datediff("column","'2016-03-09'","month") }}{{ dbt.datediff("'2016-03-09'","column","year") }}
```

**Sample Output (PostgreSQL)** :
```
((column_2)::date-(column_1)::date)((date_part('year',('2016-03-09')::date)- date_part('year',(column)::date))*12+ date_part('month',('2016-03-09')::date)- date_part('month',(column)::date))(date_part('year',(column)::date)- date_part('year',('2016-03-09')::date))
```

### date_trunc[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date_trunc "Direct link to date_trunc")
**Args** :
  * `datepart`: [date or time part](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts).
  * `date`: date/time [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).


This macro truncates / rounds a timestamp to the first instant for the given [date or time part](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts).
**Usage** :
```
{{ dbt.date_trunc("day","updated_at") }}{{ dbt.date_trunc("month","updated_at") }}{{ dbt.date_trunc("year","'2016-03-09'") }}
```

**Sample Output (PostgreSQL)** :
```
date_trunc('day', updated_at)date_trunc('month', updated_at)date_trunc('year','2016-03-09')
```

### last_day[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#last_day "Direct link to last_day")
**Args** :
  * `date`: date/time [expression](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions).
  * `datepart`: [date or time part](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts).


This macro gets the last day for a given date and datepart.
**Usage** :
  * The `datepart` argument is database-specific.
  * This macro currently only supports dateparts of `month` and `quarter`.


```
{{ dbt.last_day("created_at","month") }}{{ dbt.last_day("'2016-03-09'","year") }}
```

**Sample Output (PostgreSQL)** :
```
    date_trunc('month', created_at)+((interval'10 month')*(1))+((interval'10 day')*(-1))asdate)    date_trunc('year','2016-03-09')+((interval'10 year')*(1))+((interval'10 day')*(-1))asdate)
```

## Date and time parts[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#date-and-time-parts "Direct link to Date and time parts")
Often supported date and time parts (case insensitive):
  * `year`
  * `quarter`
  * `month`
  * `week`
  * `day`
  * `hour`
  * `minute`
  * `second`
  * `millisecond`
  * `microsecond`
  * `nanosecond`


This listing is not meant to be exhaustive, and some of these date and time parts may not be supported for particular adapters. Some macros may not support all date and time parts. Some adapters may support more or less precision.
## SQL expressions[​](https://docs.getdbt.com/reference/dbt-jinja-functions/cross-database-macros#sql-expressions "Direct link to SQL expressions")
A SQL expression may take forms like the following:
  * function
  * column name
  * date literal
  * string literal
  * <other data type> literal (number, etc)
  * `NULL`


Example: Suppose there is an `orders` table with a column named `order_date`. The following shows 3 different types of expressions:
```
select    date_trunc(month, order_date)as expression_function,    order_date as expression_column_name,'2016-03-09'as expression_date_literal,'Pennsylvania'as expression_string_literal,3as expression_number_literal,NULLas expression_null,from orders
```

Note that the string literal example includes single quotes. (Note: the string literal character may vary per database. For this example, we suppose a single quote.) To refer to a SQL string literal in Jinja, surrounding double quotes are required.
So within Jinja, the string values would be:
  * `"date_trunc(month, order_date)"`
  * `"order_date"`
  * `"'2016-03-09'"`
  * `"'Pennsylvania'"`
  * `"NULL"`


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdispatch+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdispatch+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdispatch+so+I+can+ask+questions+about+it.)
On this page
dbt can extend functionality across [Supported Data Platforms](https://docs.getdbt.com/docs/supported-data-platforms) through a system of [multiple dispatch](https://en.wikipedia.org/wiki/Multiple_dispatch). Because SQL syntax, data types, and DDL/DML support vary across adapters, dbt can define and call generic functional macros, and then "dispatch" that macro to the appropriate implementation for the current adapter.
## Syntax[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#syntax "Direct link to Syntax")
**Args** :
  * `macro_name` [required]: Name of macro to dispatch. Must be a string literal.
  * `macro_namespace` [optional]: Namespace (package) of macro to dispatch. Must be a string literal.


**Usage** :
```
{% macro my_macro(arg1, arg2)-%}  {{ return(adapter.dispatch('my_macro')(arg1, arg2)) }}{%- endmacro %}
```

dbt uses two criteria when searching for the right candidate macro:
  * Adapter prefix
  * Namespace (package)


**Adapter prefix:** Adapter-specific macros are prefixed with the lowercase adapter name and two underscores. Given a macro named `my_macro`, dbt will look for:
  * Postgres: `postgres__my_macro`
  * Redshift: `redshift__my_macro`
  * Snowflake: `snowflake__my_macro`
  * BigQuery: `bigquery__my_macro`
  * OtherAdapter: `otheradapter__my_macro`
  * _default:_ `default__my_macro`


If dbt does not find an adapter-specific implementation, it will dispatch to the default implementation.
**Namespace:** Generally, dbt will search for implementations in the root project and internal projects (e.g. `dbt`, `dbt_postgres`). If the `macro_namespace` argument is provided, it instead searches the specified namespace (package) for viable implementations. It is also possible to dynamically route namespace searching by defining a [`dispatch` project config](https://docs.getdbt.com/reference/project-configs/dispatch-config); see the examples below for details.
## Examples[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#examples "Direct link to Examples")
### A simple example[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#a-simple-example "Direct link to A simple example")
Let's say I want to define a macro, `concat`, that compiles to the SQL function `concat()` as its default behavior. On Redshift and Snowflake, however, I want to use the `||` operator instead.
macros/concat.sql
```
{% macro concat(fields)-%}    {{ return(adapter.dispatch('concat')(fields)) }}{%- endmacro %}{% macro default__concat(fields)-%}    concat({{ fields|join(', ') }}){%- endmacro %}{% macro redshift__concat(fields)%}    {{ fields|join(' || ') }}{% endmacro %}{% macro snowflake__concat(fields)%}    {{ fields|join(' || ') }}{% endmacro %}
```

The top `concat` macro follows a special, rigid formula: It is named with the macro's "primary name," `concat`, which is how the macro will be called elsewhere. It accepts one argument, named `fields`. This macro's _only_ function is to dispatch—that is, look for and return—using the primary macro name (`concat`) as its search term. It also wants to pass through, to its eventual implementation, all the keyword arguments that were passed into it. In this case, there's only one argument, named `fields`.
Below that macro, I've defined three possible implementations of the `concat` macro: one for Redshift, one for Snowflake, and one for use by default on all other adapters. Depending on the adapter I'm running against, one of these macros will be selected, it will be passed the specified arguments as inputs, it will operate on those arguments, and it will pass back the result to the original dispatching macro.
### A more complex example[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#a-more-complex-example "Direct link to A more complex example")
I found an existing implementation of the `concat` macro in the dbt-utils package. However, I want to override its implementation of the `concat` macro on Redshift in particular. In all other cases—including the default implementation—I'm perfectly happy falling back to the implementations defined in `dbt_utils.concat`.
macros/concat.sql
```
{% macro concat(fields)-%}    {{ return(adapter.dispatch('concat')(fields)) }}{%- endmacro %}{% macro default__concat(fields)-%}    {{ return(dbt_utils.concat(fields)) }}{%- endmacro %}{% macro redshift__concat(fields)%}%for field infields%}nullif({{ field }},'') {{ ' || 'ifnotloop.last }}% endfor %}{% endmacro %}
```

If I'm running on Redshift, dbt will use my version; if I'm running on any other database, the `concat()` macro will shell out to the version defined in `dbt_utils`.
## For package maintainers[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#for-package-maintainers "Direct link to For package maintainers")
Dispatched macros from [packages](https://docs.getdbt.com/docs/build/packages) _must_ provide the `macro_namespace` argument, as this declares the namespace (package) where it plans to search for candidates. Most often, this is the same as the name of your package, e.g. `dbt_utils`. (It is possible, if rarely desirable, to define a dispatched macro _not_ in the `dbt_utils` package, and dispatch it into the `dbt_utils` namespace.)
Here we have the definition of the `dbt_utils.concat` macro, which specifies both the `macro_name` and `macro_namespace` to dispatch:
```
{% macro concat(fields)-%}  {{ return(adapter.dispatch('concat','dbt_utils')(fields)) }}{%- endmacro %}
```

### Overriding package macros[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#overriding-package-macros "Direct link to Overriding package macros")
Following the second example above: Whenever I call my version of the `concat` macro in my own project, it will use my special null-handling version on Redshift. But the version of the `concat` macro _within_ the dbt-utils package will not use my version.
Why does this matter? Other macros in dbt-utils, such as `surrogate_key`, call the `dbt_utils.concat` macro directly. What if I want `dbt_utils.surrogate_key` to use _my_ version of `concat` instead, including my custom logic on Redshift?
As a user, I can accomplish this via a [project-level `dispatch` config](https://docs.getdbt.com/reference/project-configs/dispatch-config). When dbt goes to dispatch `dbt_utils.concat`, it knows from the `macro_namespace` argument to search in the `dbt_utils` namespace. The config below defines dynamic routing for that namespace, telling dbt to search through an ordered sequence of packages, instead of just the `dbt_utils` package.
dbt_project.yml
```
dispatch:-macro_namespace: dbt_utilssearch_order:['my_project','dbt_utils']
```

Note that this config _must_ be specified in the user's root `dbt_project.yml`. dbt will ignore any `dispatch` configs defined in the project files of installed packages.
Adapter prefixes still matter: dbt will only ever look for implementations that are compatible with the current adapter. But dbt will prioritize package specificity over adapter specificity. If I call the `concat` macro while running on Postgres, with the config above, dbt will look for the following macros in order:
  1. `my_project.postgres__concat` (not found)
  2. `my_project.default__concat` (not found)
  3. `dbt_utils.postgres__concat` (not found)
  4. `dbt_utils.default__concat` (found! use this one)


As someone installing a package, this functionality makes it possible for me to change the behavior of another, more complex macro (`dbt_utils.surrogate_key`) by reimplementing and overriding one of its modular components.
As a package maintainer, this functionality enables users of my package to extend, reimplement, or override default behavior, without needing to fork the package's source code.
### Overriding global macros[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#overriding-global-macros "Direct link to Overriding global macros")
Certain functions like [`ref`](https://docs.getdbt.com/reference/dbt-jinja-functions/ref), [`source`](https://docs.getdbt.com/reference/dbt-jinja-functions/source), and [`config`](https://docs.getdbt.com/reference/dbt-jinja-functions/config) can't be overridden with a package using the dispatch config. This is because `ref`, `source`, and `config` are context properties within dbt and are not dispatched as global macros. Refer to [this GitHub discussion](https://github.com/dbt-labs/dbt-core/issues/4491#issuecomment-994709916) for more context.
I maintain an internal utility package at my organization, named `my_org_dbt_helpers`. I use this package to reimplement built-in dbt macros on behalf of all my dbt-using colleagues, who work across a number of dbt projects.
My package can define custom versions of any dispatched global macro I choose, from `generate_schema_name` to `test_unique`. I can define a new default version of that macro (e.g. `default__generate_schema_name`), or custom versions for specific data warehouse adapters (e.g. `spark__generate_schema_name`).
Each root project installing my package simply needs to include the [project-level `dispatch` config](https://docs.getdbt.com/reference/project-configs/dispatch-config) that searches my package ahead of `dbt` for the `dbt` global namespace:
dbt_project.yml
```
dispatch:-macro_namespace: dbtsearch_order:['my_project','my_org_dbt_helpers','dbt']
```

### Managing different global overrides across packages[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#managing-different-global-overrides-across-packages "Direct link to Managing different global overrides across packages")
You can override global behaviors in different ways for each project that is installed as a package. This holds true for all global macros: `generate_schema_name`, `create_table_as`, etc. When parsing or running a resource defined in a package, the definition of the global macro within that package takes precedence over the definition in the root project because it's more specific to those resources.
By combining package-level overrides and `dispatch`, it is possible to achieve three different patterns:
  1. **Package always wins** — As the developer of dbt models in a project that will be deployed elsewhere as a package, You want full control over the macros used to define & materialize my models. Your macros should always take precedence for your models, and there should not be any way to override them.
     * _Mechanism:_ Each project/package fully overrides the macro by its name, for example, `generate_schema_name` or `create_table_as`. Do not use dispatch.
  2. **Conditional application (root project wins)** — As the maintainer of one dbt project in a mesh of multiple, your team wants conditional application of these rules. When running your project standalone (in development), you want to apply custom behavior; but when installed as a package and deployed alongside several other projects (in production), you want the root-level project's rules to apply.
     * _Mechanism:_ Each package implements its "local" override by registering a candidate for dispatch with an adapter prefix, for example, `default__generate_schema_name` or `default__create_table_as`. The root-level project can then register its own candidate for dispatch (`default__generate_schema_name`), winning the default search order or by explicitly overriding the macro by name (`generate_schema_name`).
  3. **Same rules everywhere all the time** — As a member of the data platform team responsible for consistency across teams at your organization, you want to create a "macro package" that every team can install & use.
     * _Mechanism:_ Create a standalone package of candidate macros only, for example, `default__generate_schema_name` or `default__create_table_as`. Add a [project-level `dispatch` configuration](https://docs.getdbt.com/reference/project-configs/dispatch-config) in every project's `dbt_project.yml`.


## For adapter plugin maintainers[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#for-adapter-plugin-maintainers "Direct link to For adapter plugin maintainers")
Most packages were initially designed to work on the four original dbt adapters. By using the `dispatch` macro and project config, it is possible to "shim" existing packages to work on other adapters, by way of third-party compatibility packages.
For instance, if I want to use `dbt_utils.concat` on Apache Spark, I can install a compatibility package, spark-utils, alongside dbt-utils:
packages.yml
```
packages:-package: dbt-labs/dbt_utilsversion:...-package: dbt-labs/spark_utilsversion:...
```

I then include `spark_utils` in the search order for dispatched macros in the `dbt_utils` namespace. (I still include my own project first, just in case I want to reimplement any macros with my own custom logic.)
dbt_project.yml
```
dispatch:-macro_namespace: dbt_utilssearch_order:['my_project','spark_utils','dbt_utils']
```

When dispatching `dbt_utils.concat`, dbt will search for:
  1. `my_project.spark__concat` (not found)
  2. `my_project.default__concat` (not found)
  3. `spark_utils.spark__concat` (found! use this one)
  4. `spark_utils.default__concat`
  5. `dbt_utils.postgres__concat`
  6. `dbt_utils.default__concat`


As a compatibility package maintainer, I only need to reimplement the foundational building-block macros which encapsulate low-level syntactical differences. By reimplementing low-level macros, such as `spark__dateadd` and `spark__datediff`, the `spark_utils` package provides access to more complex macros (`dbt_utils.date_spine`) "for free."
As a `dbt-spark` user, by installing `dbt_utils` and `spark_utils` together, I don't just get access to higher-level utility macros. I may even be able to install and use packages with no Spark-specific logic, and which have never been tested against Spark, so long as they rely on `dbt_utils` macros for cross-adapter compatibility.
### Adapter inheritance[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#adapter-inheritance "Direct link to Adapter inheritance")
Some adapters "inherit" from other adapters (e.g. `dbt-postgres` → `dbt-redshift`, and `dbt-spark` → `dbt-databricks`). If using a child adapter, dbt will include any parent adapter implementations in its search order, too. Instead of just looking for `redshift__` and falling back to `default__`, dbt will look for `redshift__`, `postgres__`, and `default__`, in that order.
Child adapters tend to have very similar SQL syntax to their parents, so this allows them to skip reimplementing a macro that has already been reimplemented by the parent adapter.
Following the example above with `dbt_utils.concat`, the full search order on Redshift is actually:
  1. `my_project.redshift__concat`
  2. `my_project.postgres__concat`
  3. `my_project.default__concat`
  4. `dbt_utils.redshift__concat`
  5. `dbt_utils.postgres__concat`
  6. `dbt_utils.default__concat`


In rare cases, the child adapter may prefer the default implementation to its parent's adapter-specific implementation. In that case, the child adapter should define an adapter-specific macro that calls the default. For instance, the PostgreSQL syntax for adding dates ought to work on Redshift, too, but I may happen to prefer the simplicity of `dateadd`:
```
{% macro dateadd(datepart,interval, from_date_or_timestamp)%}    {{ return(adapter.dispatch('dateadd')(datepart,interval, from_date_or_timestamp)) }}{% endmacro %}{% macro default__dateadd(datepart,interval, from_date_or_timestamp)%}    dateadd({{ datepart }}, {{ interval }}, {{ from_date_or_timestamp }}){% endmacro %}{% macro postgres__dateadd(datepart,interval, from_date_or_timestamp)%}    {{ from_date_or_timestamp }} +((interval'1 {{ datepart }}')*({{ interval }})){% endmacro %}{# Use default syntax instead of postgres syntax #}{% macro redshift__dateadd(datepart,interval, from_date_or_timestamp)%}    {{ return(default__dateadd(datepart,interval, from_date_or_timestamp) }}{% endmacro %}
```

## FAQs[​](https://docs.getdbt.com/reference/dbt-jinja-functions/dispatch#faqs "Direct link to FAQs")
[Error] Could not find my_project package
If a package name is included in the `search_order` of a project-level `dispatch` config, dbt expects that package to contain macros which are viable candidates for dispatching. If an included package does not contain _any_ macros, dbt will raise an error like:
```
Compilation Error  In dispatch: Could not find package 'my_project'
```

This does not mean the package or root project is missing—it means that any macros from it are missing, and so it is missing from the search spaces available to `dispatch`.
If you've tried the step above and are still experiencing this behavior - reach out to the Support team at support@getdbt.com and we'll be happy to help!
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/doc ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/doc?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdoc+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdoc+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fdoc+so+I+can+ask+questions+about+it.)
The `doc` function is used to reference docs blocks in the description field of schema.yml files. It is analogous to the `ref` function. For more information, consult the [Documentation guide](https://docs.getdbt.com/docs/explore/build-and-view-your-docs).
Usage:
orders.md
```
{% docs orders %}# docs- go- here{% enddocs %}
```

schema.yml
```
models:-name: ordersdescription:"{{ doc('orders') }}"
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/builtins ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/builtins?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fbuiltins+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fbuiltins+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fbuiltins+so+I+can+ask+questions+about+it.)
On this page
The `builtins` variable exists to provide references to builtin dbt context methods. This allows macros to be created with names that _mask_ dbt builtin context methods, while still making those methods accessible in the dbt compilation context.
The `builtins` variable is a dictionary containing the following keys:


## Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/builtins?version=1.12#usage "Direct link to Usage")
Using the `builtins` variable in this way is an advanced development workflow. Users should be ready to maintain and update these overrides when upgrading in the future.
From dbt v1.5 and higher, use the following macro to override the `ref` method available in the model compilation context to return a [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) with the database name overriden to `dev`.
It includes logic to extract user-provided arguments, including `version`, and call the `builtins.ref()` function with either a single `modelname` argument or both `packagename` and `modelname` arguments, based on the number of positional arguments in `varargs`.
Note that the `ref`, `source`, and `config` functions can't be overridden with a package. This is because `ref`, `source`, and `config` are context properties within dbt and are not dispatched as global macros. Refer to [this GitHub discussion](https://github.com/dbt-labs/dbt-core/issues/4491#issuecomment-994709916) for more context.
```
{% macro ref() %}-- extract user-provided positional and keyword arguments{% set version = kwargs.get('version') or kwargs.get('v') %}{% set packagename = none %}{%- if (varargs | length) == 1 -%}    {% set modelname = varargs[0] %}{%- else -%}    {% set packagename = varargs[0] %}    {% set modelname = varargs[1] %}{% endif %}-- call builtins.ref based on provided positional arguments{% set rel = None %}{% if packagename is not none %}    {% set rel = builtins.ref(packagename, modelname, version=version) %}{% else %}    {% set rel = builtins.ref(modelname, version=version) %}{% endif %}-- finally, override the database name with "dev"{% set newrel = rel.replace_path(database="dev") %}{% do return(newrel) %}{% endmacro %}
```

Logic within the ref macro can also be used to control which elements of the model path are rendered when run, for example the following logic renders only the schema and object identifier, but not the database reference i.e. `my_schema.my_model` rather than `my_database.my_schema.my_model`. This is especially useful when using snowflake as a warehouse, if you intend to change the name of the database post-build and wish the references to remain accurate.
```
  -- render identifiers without a database  {% do return(rel.include(database=false)) %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Was this page helpful?](https://docs.getdbt.com/reference/dbt-jinja-functions/builtins?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/invocation_id ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/invocation_id?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Finvocation_id+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Finvocation_id+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Finvocation_id+so+I+can+ask+questions+about+it.)
The `invocation_id` outputs a UUID generated for this dbt command. This value is useful when auditing or analyzing dbt invocation metadata.
If available, the `invocation_id` is:
  * available in the compilation context of [`query-comment`](https://docs.getdbt.com/reference/project-configs/query-comment)
  * included in the `info` dictionary in dbt [events and logs](https://docs.getdbt.com/reference/events-logging#info)
  * included in the `metadata` dictionary in [dbt artifacts](https://docs.getdbt.com/reference/artifacts/dbt-artifacts#common-metadata)
  * included as a label in all BigQuery jobs that dbt originates


**Example usage** : You can use the following example code for all data platforms. Remember to replace `TABLE_NAME` with the actual name of your target table:
`select '{{ invocation_id }}' as test_id from TABLE_NAME`
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/log ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/log?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Flog+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Flog+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Flog+so+I+can+ask+questions+about+it.)
**Args** :
  * `msg`: The message (string) to log
  * `info`: If False, write to the log file. If True, write to both the log file and stdout (default=False)


Logs a line to either the log file or stdout.
Details
Code source Refer to [GitHub](https://github.com/dbt-labs/dbt-core/blob/HEAD/core/dbt/context/base.py#L549-L566) or the following code as a source:
```
deflog(msg:str, info:bool=False)-str:"""Logs a line to either the log file or stdout.        :param msg: The message to log        :param info: If `False`, write to the log file. If `True`, write to            both the log file and stdout.        > macros/my_log_macro.sql            {% macro some_macro(arg1, arg2) %}              {{ log("Running some_macro: " ~ arg1 ~ ", " ~ arg2) }}            {% endmacro %}"if info:            fire_event(JinjaLogInfo(msg=msg, node_info=get_node_info()))            fire_event(JinjaLogDebug(msg=msg, node_info=get_node_info()))return""
```

```
{% macro some_macro(arg1, arg2)%}	{{ log("Running some_macro: "~ arg1 ~", "~ arg2) }}{% endmacro %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/graph ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fgraph+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fgraph+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fgraph+so+I+can+ask+questions+about+it.)
On this page
The `graph` context variable contains information about the _nodes_ in your dbt project. Models, sources, tests, and snapshots are all examples of nodes in dbt projects.
dbt actively builds the `graph` variable during the [parsing phase](https://docs.getdbt.com/reference/dbt-jinja-functions/execute) of running dbt projects, so some properties of the `graph` context variable will be missing or incorrect during parsing. Please read the information below carefully to understand how to effectively use this variable.
### The graph context variable[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#the-graph-context-variable "Direct link to The graph context variable")
The `graph` context variable is a dictionary which maps node ids onto dictionary representations of those nodes. A simplified example might look like:
```
"nodes":{"model.my_project.model_name":{"unique_id":"model.my_project.model_name","config":{"materialized":"table","sort":"id"},"tags":["abc","123"],"path":"models/path/to/model_name.sql","sources":{"source.my_project.snowplow.event":{"unique_id":"source.my_project.snowplow.event","database":"analytics","schema":"analytics","tags":["abc","123"],"path":"models/path/to/schema.yml","exposures":{"exposure.my_project.traffic_dashboard":{"unique_id":"exposure.my_project.traffic_dashboard","type":"dashboard","maturity":"high","path":"models/path/to/schema.yml","metrics":{"metric.my_project.count_all_events":{"unique_id":"metric.my_project.count_all_events","type":"count","path":"models/path/to/schema.yml","groups":{"group.my_project.finance":{"unique_id":"group.my_project.finance","name":"finance","owner":{"email":"finance@jaffleshop.com"
```

The exact contract for these model and source nodes is not currently documented, but that will change in the future.
### Accessing models[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#accessing-models "Direct link to Accessing models")
The `model` entries in the `graph` dictionary will be incomplete or incorrect during parsing. If accessing the models in your project via the `graph` variable, be sure to use the [execute](https://docs.getdbt.com/reference/dbt-jinja-functions/execute) flag to ensure that this code only executes at run-time and not at parse-time. Do not use the `graph` variable to build your DAG, as the resulting dbt behavior will be undefined and likely incorrect. Example usage:
graph-usage.sql
```
  Print information about all of the models in the Snowplow package{%ifexecute%}%for node in graph.nodes.values()| selectattr("resource_type","equalto","model")| selectattr("package_name","equalto","snowplow")%}%do log(node.unique_id ~", materialized: "~ node.config.materialized, info=true)%}% endfor %}{% endif %}  Example output---------------------------------------------------------------model.snowplow.snowplow_id_map, materialized: incrementalmodel.snowplow.snowplow_page_views, materialized: incrementalmodel.snowplow.snowplow_web_events, materialized: incrementalmodel.snowplow.snowplow_web_page_context, materialized: tablemodel.snowplow.snowplow_web_events_scroll_depth, materialized: incrementalmodel.snowplow.snowplow_web_events_time, materialized: incrementalmodel.snowplow.snowplow_web_events_internal_fixed, materialized: ephemeralmodel.snowplow.snowplow_base_web_page_context, materialized: ephemeralmodel.snowplow.snowplow_base_events, materialized: ephemeralmodel.snowplow.snowplow_sessions_tmp, materialized: incrementalmodel.snowplow.snowplow_sessions, materialized: table
```

### Accessing sources[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#accessing-sources "Direct link to Accessing sources")
To access the sources in your dbt project programmatically, use the `sources` attribute of the `graph` object.
Example usage:
models/events_unioned.sql
```
  Union all of the Snowplow sources defined in the project  which begin with the string "event_"{%set sources =[]-%}{%for node in graph.sources.values()-%}%-if node.name.startswith('event_')and node.source_name =='snowplow'-%}%-do sources.append(source(node.source_name, node.name))-%}%- endif -%}{%- endfor %}select*from(%-for source in sources %}select*from {{ source }} {%ifnotloop.last%} unionall {% endif %}% endfor %}  Example compiled SQL---------------------------------------------------------------select * from (  select * from raw.snowplow.event_add_to_cart union all  select * from raw.snowplow.event_remove_from_cart union all  select * from raw.snowplow.event_checkout
```

### Accessing exposures[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#accessing-exposures "Direct link to Accessing exposures")
To access the exposures in your dbt project programmatically, use the `exposures` attribute of the `graph` object.
Example usage:
models/my_important_view_model.sql
```
{# Include a SQL comment naming all of the exposures that this model feeds into #}{%set exposures =[]-%}{%for exposure in graph.exposures.values()-%}%-if model['unique_id']in exposure.depends_on.nodes -%}%-do exposures.append(exposure)-%}%- endif -%}{%- endfor %}-- HELLO database administrator! Before dropping this view,-- please be aware that doing so will affect:{%for exposure in exposures %}--   * {{ exposure.name }} ({{ exposure.type }}){% endfor %}  Example compiled SQL----------------------------------------------------------------- HELLO database administrator! Before dropping this view,-- please be aware that doing so will affect:--   * our_metrics (dashboard)--   * my_sync (application)
```

### Accessing metrics[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#accessing-metrics "Direct link to Accessing metrics")
To access the metrics in your dbt project programmatically, use the `metrics` attribute of the `graph` object.
Example usage:
macros/get_metric.sql
```
{% macro get_metric_sql_for(metric_name)%}%set metrics = graph.metrics.values()%}%set metric =(metrics | selectattr('name','equalto', metric_name)| list).pop()%}/* Elsewhere, I've defined a macro, get_metric_timeseries_sql, that will return      the SQL needed to perform a time-based rollup of this metric's calculation */%set metric_sql = get_metric_timeseries_sql(      relation = metric['model'],type= metric['type'],      expression = metric['sql'],  {{ return(metric_sql) }}{% endmacro %}
```

### Accessing groups[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#accessing-groups "Direct link to Accessing groups")
To access the groups in your dbt project programmatically, use the `groups` attribute of the `graph` object.
Example usage:
macros/get_group.sql
```
{% macro get_group_owner_for(group_name)%}%set groups = graph.groups.values()%}%set owner =(groups | selectattr('owner','equalto', group_name)| list).pop()%}  {{ return(owner) }}{% endmacro %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [The graph context variable](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#the-graph-context-variable)[​](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#the-graph-context-variable "Direct link to The graph context variable")
  * [Was this page helpful?](https://docs.getdbt.com/reference/dbt-jinja-functions/graph?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/local_md5 ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/local_md5?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Flocal_md5+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Flocal_md5+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Flocal_md5+so+I+can+ask+questions+about+it.)
The `local_md5` context variable calculates an [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the given string. The string `local_md5` emphasizes that the hash is calculated _locally_ , in the dbt-Jinja context. This variable is typically useful for advanced use cases. For example, when you generate unique identifiers within custom materialization or operational logic, you can either avoid collisions between temporary relations or identify changes by comparing checksums.
It is different than the `md5` SQL function, supported by many SQL dialects, which runs remotely in the data platform. You want to always use SQL hashing functions when generating surrogate keys
Usage:
```
-- source{%-set value_hash = local_md5("hello world")-%}'{{ value_hash }}'-- compiled'5eb63bbbe01eeed093cb22bb8f5acdc3'
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/project_name ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/project_name#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fproject_name+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fproject_name+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fproject_name+so+I+can+ask+questions+about+it.)
On this page
The `project_name` context variable returns the `name` for the root-level project which is being run by dbt. This variable can be used to defer execution to a root-level project macro if one exists.
### Example Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/project_name#example-usage "Direct link to Example Usage")
redshift/macros/helper.sql
```
  This macro vacuums tables in a Redshift database. If a macro exists in the  root-level project called `get_tables_to_vacuum`, this macro will call _that_  macro to find the tables to vacuum. If the macro is not defined in the root  project, this macro will use a default implementation instead.{% macro vacuum_tables()%}%set root_project = context[project_name]%}%if root_project.get_tables_to_vacuum %}%settables= root_project.get_tables_to_vacuum()%}%else%}%settables= redshift.get_tables_to_vacuum()%}% endif %}%fortableintables%}%do redshift.vacuum_table(table)%}% endfor %}{% endmacro %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/return ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/return#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Freturn+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Freturn+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Freturn+so+I+can+ask+questions+about+it.)
**Args** :
  * `data`: The data to return to the caller


The `return` function can be used in macros to return data to the caller. The type of the data (dict, list, int, etc) will be preserved through the `return` call. You can use the `return` function in the following ways within your macros: as an expression or as a statement.
  * Expression — Use an expression when the goal is to output a string from the macro.
  * Statement with a `do` tag — Use a statement with a `do` tag to execute the return function without generating an output string. This is particularly useful when you want to perform actions without necessarily inserting their results directly into the template.


In the following example, `{{ return([1,2,3]) }}` acts as an _expression_ that directly outputs a string, making it suitable for directly inserting returned values into SQL code.
macros/get_data.sql
```
{% macro get_data()%}  {{ return([1,2,3]) }}{% endmacro %}
```

Alternatively, you can use a statement with a [do](https://jinja.palletsprojects.com/en/3.0.x/extensions/#expression-statement) tag (or expression-statements) to execute the return function without generating an output string.
In the following example ,`{% do return([1,2,3]) %}` acts as a _statement_ that executes the return action but does not output a string:
macros/get_data.sql
```
{% macro get_data()%}%doreturn([1,2,3])%}{% endmacro %}
```

models/my_model.sql
```
select-- getdata() returns a list!%forin get_data()%}    {{ i }}%-ifnotloop.last%},{% endif -%}% endfor %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/model ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/model#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fmodel+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fmodel+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fmodel+so+I+can+ask+questions+about+it.)
On this page
`model` is the dbt [graph object](https://docs.getdbt.com/reference/dbt-jinja-functions/graph) (or node) for the current model. It can be used to:
  * Access `config` settings, say, in a post-hook
  * Access the path to the model


For example:
```
{% if model.config.materialized == 'view' %}  {{ log(model.name ~ " is a view.", info=True) }}{% endif %}
```

To view the contents of `model` for a given model:
  * Command line interface
  * Studio IDE


If you're using the command line interface (CLI), use [log()](https://docs.getdbt.com/reference/dbt-jinja-functions/log) to print the full contents:
```
{{ log(model, info=True) }}
```

If you're using the Studio IDE, compile the following to print the full contents:
```
{{ model | tojson(indent = 4) }}
```

## Batch properties for microbatch models[​](https://docs.getdbt.com/reference/dbt-jinja-functions/model#batch-properties-for-microbatch-models "Direct link to Batch properties for microbatch models")
Starting in dbt Core v1.9, the model object includes a `batch` property (`model.batch`), which provides details about the current batch when executing an [incremental microbatch](https://docs.getdbt.com/docs/build/incremental-microbatch) model. This property is only populated during the batch execution of a microbatch model.
The following table describes the properties of the `batch` object. Note that dbt appends the property to the `model` and `batch` objects.
Property | Description | Example
---|---|---
The unique identifier for the batch within the context of the microbatch model. | `model.batch.id`
`event_time_start` | The start time of the batch's [`event_time`](https://docs.getdbt.com/reference/resource-configs/event-time) filter (inclusive). | `model.batch.event_time_start`
`event_time_end` | The end time of the batch's `event_time` filter (exclusive). | `model.batch.event_time_end`
Loading table...
---
### Usage notes[​](https://docs.getdbt.com/reference/dbt-jinja-functions/model#usage-notes "Direct link to Usage notes")
`model.batch` is only available during the execution of a microbatch model batch. Outside of the microbatch execution, `model.batch` is `None`, and its sub-properties aren't accessible.
#### Example of safeguarding access to batch properties[​](https://docs.getdbt.com/reference/dbt-jinja-functions/model#example-of-safeguarding-access-to-batch-properties "Direct link to Example of safeguarding access to batch properties")
We recommend to always check if `model.batch` is populated before accessing its properties. To do this, use an `if` statement for safe access to `batch` properties:
```
{% if model.batch %}  {{ log(model.batch.id) }}  # Log the batch ID #  {{ log(model.batch.event_time_start) }}  # Log the start time of the batch #  {{ log(model.batch.event_time_end) }}  # Log the end time of the batch #{% endif %}
```

In this example, the `if model.batch` statement makes sure that the code only runs during a batch execution. `log()` is used to print the `batch` properties for debugging.
#### Example of log batch details[​](https://docs.getdbt.com/reference/dbt-jinja-functions/model#example-of-log-batch-details "Direct link to Example of log batch details")
This is a practical example of how you might use `model.batch` in a microbatch model to log batch details for the `batch.id`:
```
{% if model.batch %}  {{ log("Processing batch with ID: " ~ model.batch.id, info=True) }}  {{ log("Batch event time range: " ~ model.batch.event_time_start ~ " to " ~ model.batch.event_time_end, info=True) }}{% endif %}
```

In this example, the `if model.batch` statement makes sure that the code only runs during a batch execution. `log()` is used to print the `batch` properties for debugging.
## Model structure and JSON schema[​](https://docs.getdbt.com/reference/dbt-jinja-functions/model#model-structure-and-json-schema "Direct link to Model structure and JSON schema")
To view the structure of `models` and their definitions:
  * Refer to [dbt JSON Schema](https://schemas.getdbt.com/) for describing and consuming dbt generated artifacts
  * Select the corresponding manifest version under **Manifest**. For example if you're on dbt v1.8, then you would select Manifest v12
    * The `manifest.json` version number is related to (but not _equal_ to) your dbt version, so you _must_ use the correct `manifest.json` version for your dbt version. To find the correct `manifest.json` version, refer to [Manifest](https://docs.getdbt.com/reference/artifacts/manifest-json) and select the dbt version on the top navigation (such as `v1.5`). This will help you find out which tags are associated with your model.
  * Then go to `nodes` --> Select Additional properties --> `CompiledModelNode` or view other definitions/objects.


Use the following table to understand how the versioning pattern works and match the Manifest version with the dbt version:
dbt version | Manifest version
---|---
dbt Fusion engine v2.0 | v20 (Identical to [v12](https://schemas.getdbt.com/dbt/manifest/v12/index.html))
Core v1.11
Core v1.10
Core v1.9
Core v1.8
Core v1.7
Core v1.6
Core v1.5
Core v1.4
Core v1.3
Loading table...
---
## Related docs[​](https://docs.getdbt.com/reference/dbt-jinja-functions/model#related-docs "Direct link to Related docs")
  * [dbt JSON Schema](https://schemas.getdbt.com/)


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/packages.yml context ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/packages.yml%20context#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fpackages.yml%2520context+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fpackages.yml%2520context+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fpackages.yml%2520context+so+I+can+ask+questions+about+it.)
On this page
The following context methods and variables are available when configuring a `packages.yml` file.
**Available context methods:**
  * [env_var](https://docs.getdbt.com/reference/dbt-jinja-functions/env_var)
    * Use `env_var()` in any dbt YAML file that supports Jinja. Only `packages.yml` and `profiles.yml` support environment variables for [secure values](https://docs.getdbt.com/docs/build/dbt-tips#yaml-tips) (using the `DBT_ENV_SECRET_` prefix).
  * [var](https://docs.getdbt.com/reference/dbt-jinja-functions/var) (Note: only variables defined with `--vars` are available. Refer to [YAML tips](https://docs.getdbt.com/docs/build/dbt-tips#yaml-tips) for more information)


**Available context variables:**


## Example usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/packages.yml%20context#example-usage "Direct link to Example usage")
The following examples show how to use the different context methods and variables in your `packages.yml`.
Use `builtins` in your `packages.yml`:
```
packages:  - package: dbt-labs/dbt_utils    version: "{% if builtins is defined %}0.14.0{% else %}0.13.1{% endif %}"
```

Use `env_var` in your `packages.yml`:
```
packages:  - package: dbt-labs/dbt_utils    version: "{{ env_var('DBT_UTILS_VERSION') }}"
```

Use `dbt_version` in your `packages.yml`:
```
packages:  - package: dbt-labs/dbt_utils    version: "{% if dbt_version is defined %}0.14.0{% else %}0.13.1{% endif %}"
```

Use `target` in your `packages.yml`:
```
packages:  - package: dbt-labs/dbt_utils    version: "{% if target.name == 'prod' %}0.14.0{% else %}0.13.1{% endif %}"
```

## Related docs[​](https://docs.getdbt.com/reference/dbt-jinja-functions/packages.yml%20context#related-docs "Direct link to Related docs")


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/print ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/print#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fprint+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fprint+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fprint+so+I+can+ask+questions+about+it.)
On this page
Use the `print()` function when you want to print messages to both the log file and standard output (stdout).
When used in conjunction with the `QUIET` global config, which suppresses non-error logs, you will only see error logs and the print messages in stdout. For more information, see [Global configs](https://docs.getdbt.com/reference/global-configs/about-global-configs).
## Example[​](https://docs.getdbt.com/reference/dbt-jinja-functions/print#example "Direct link to Example")
```
% macro some_macro(arg1, arg2)%}    {{ print("Running some_macro: "~ arg1 ~", "~ arg2) }}% endmacro %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/profiles-yml-context ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/profiles-yml-context#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fprofiles-yml-context+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fprofiles-yml-context+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fprofiles-yml-context+so+I+can+ask+questions+about+it.)
On this page
The following context methods are available when configuring resources in the `profiles.yml` file.
**Available context methods:**
  * [var](https://docs.getdbt.com/reference/dbt-jinja-functions/var) (_Note: only variables defined with`--vars` are available_)


### Example usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/profiles-yml-context#example-usage "Direct link to Example usage")
~/.dbt/profiles.yml
```
jaffle_shop:target: devoutputs:type: redshifthost:"{{ env_var('DBT_HOST') }}"user:"{{ env_var('DBT_USER') }}"password:"{{ env_var('DBT_PASS') }}"port:5439dbname: analyticsschema: dbt_dbaninthreads:4
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/modules ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/modules?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fmodules+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fmodules+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fmodules+so+I+can+ask+questions+about+it.)
On this page
The `modules` variable in the Jinja context contains useful Python modules for operating on data.
## datetime[​](https://docs.getdbt.com/reference/dbt-jinja-functions/modules?version=1.12#datetime "Direct link to datetime")
This variable is a pointer to the Python [datetime](https://docs.python.org/3/library/datetime.html) module, which supports complex date and time logic.
It includes the modules contexts of `date`, `datetime`, `time`, `timedelta`, and `tzinfo`.
**Usage**
```
{% set now = modules.datetime.datetime.now() %}{% set three_days_ago_iso = (now - modules.datetime.timedelta(3)).isoformat() %}
```

This module will return the current date and time on every Jinja evaluation. For the date and time of the start of the run, please see [run_started_at](https://docs.getdbt.com/reference/dbt-jinja-functions/run_started_at).
## pytz[​](https://docs.getdbt.com/reference/dbt-jinja-functions/modules?version=1.12#pytz "Direct link to pytz")
This variable is a pointer to the Python [pytz](https://pypi.org/project/pytz/) module, which supports timezone logic.
**Usage**
```
{% set dt = modules.datetime.datetime(2002, 10, 27, 6, 0, 0) %}{% set dt_local = modules.pytz.timezone('US/Eastern').localize(dt) %}{{ dt_local }}
```

## re[​](https://docs.getdbt.com/reference/dbt-jinja-functions/modules?version=1.12#re "Direct link to re")
This variable is a pointer to the Python [re](https://docs.python.org/3/library/re.html) module, which supports regular expressions.
**Usage**
```
{% set my_string = 's3://example/path' %}{% set s3_path_pattern = 's3://[a-z0-9-_/]+' %}{% set re = modules.re %}{% set is_match = re.match(s3_path_pattern, my_string, re.IGNORECASE) %}{% if not is_match %}    {%- do exceptions.raise_compiler_error(        my_string ~ ' is not a valid s3 path'    ) -%}{% endif %}
```

## itertools[​](https://docs.getdbt.com/reference/dbt-jinja-functions/modules?version=1.12#itertools "Direct link to itertools")
Starting in `dbt-core==1.10.6`, using `modules.itertools` raises a deprecation warning. For more information and suggested workarounds, refer to the [documentation on `ModulesItertoolsUsageDeprecation`](https://docs.getdbt.com/reference/deprecations#modulesitertoolsusagedeprecation).
This variable is a pointer to the Python [itertools](https://docs.python.org/3/library/itertools.html) module, which includes useful functions for working with iterators (loops, lists, and the like).
The supported functions are:
  * `count`
  * `cycle`
  * `repeat`
  * `accumulate`
  * `chain`
  * `compress`
  * `islice`
  * `starmap`
  * `tee`
  * `zip_longest`
  * `product`
  * `permutations`
  * `combinations`
  * `combinations_with_replacement`


**Usage**
```
{%- set A = [1, 2] -%}{%- set B = ['x', 'y', 'z'] -%}{%- set AB_cartesian = modules.itertools.product(A, B) -%}{%- for item in AB_cartesian %}  {{ item }}{%- endfor -%}
```

```
  (1, 'x')  (1, 'y')  (1, 'z')  (2, 'x')  (2, 'y')  (2, 'z')
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/run_started_at ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/run_started_at?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Frun_started_at+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Frun_started_at+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Frun_started_at+so+I+can+ask+questions+about+it.)
`run_started_at` outputs the timestamp that this run started, e.g. `2017-04-21 01:23:45.678`.
The `run_started_at` variable is a Python `datetime` object. As of 0.9.1, the timezone of this variable defaults to UTC.
run_started_at_example.sql
```
select'{{ run_started_at.strftime("%Y-%m-%d") }}'as date_dayfrom...
```

To modify the timezone of this variable, use the `pytz` module:
run_started_at_utc.sql
```
select'{{ run_started_at.astimezone(modules.pytz.timezone("America/New_York")) }}'as run_started_estfrom...
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/on-run-end-context ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/on-run-end-context?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fon-run-end-context+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fon-run-end-context+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fon-run-end-context+so+I+can+ask+questions+about+it.)
On this page
These variables are only available in the context for `on-run-end` hooks. They will evaluate to `none` if used outside of an `on-run-end` hook!
## schemas[​](https://docs.getdbt.com/reference/dbt-jinja-functions/on-run-end-context?version=1.12#schemas "Direct link to schemas")
The `schemas` context variable can be used to reference the schemas that dbt has built models into during a run of dbt. This variable can be used to grant usage on these schemas to certain users at the end of a dbt run.
Example:
dbt_project.yml
```
on-run-end:-"{% for schema in schemas %}grant usage on schema {{ schema }} to db_reader;{% endfor %}"
```

In practice, it might not be a bad idea to put this code into a macro:
macros/grants.sql
```
{% macro grant_usage_to_schemas(schemas, user) %}  {% for schema in schemas %}    grant usage on schema {{ schema }} to {{ user }};  {% endfor %}{% endmacro %}
```

dbt_project.yml
```
on-run-end:-"{{ grant_usage_to_schemas(schemas, 'user') }}"
```

## database_schemas[​](https://docs.getdbt.com/reference/dbt-jinja-functions/on-run-end-context?version=1.12#database_schemas "Direct link to database_schemas")
The `database_schemas` context variable can be used to reference the databases _and_ schemas that dbt has built models into during a run of dbt. This variable is similar to the `schemas` variable, and should be used if a dbt run builds resources into multiple different databases.
Example:
macros/grants.sql
```
{% macro grant_usage_to_schemas(database_schemas, user) %}  {% for (database, schema) in database_schemas %}    grant usage on {{ database }}.{{ schema }} to {{ user }};  {% endfor %}{% endmacro %}
```

dbt_project.yml
```
on-run-end:-"{{ grant_usage_to_schemas(database_schemas, user) }}"
```

## Results[​](https://docs.getdbt.com/reference/dbt-jinja-functions/on-run-end-context?version=1.12#results "Direct link to Results")
The `results` variable contains a list of [Result objects](https://docs.getdbt.com/reference/dbt-classes#result-objects) with one element per resource that executed in the dbt job. The Result object provides access within the Jinja on-run-end context to the information that will populate the [run results JSON artifact](https://docs.getdbt.com/reference/artifacts/run-results-json).
Example usage:
macros/log_results.sql
```
{% macro log_results(results)%}%ifexecute%}  {{ log("========== Begin Summary ==========", info=True) }}%for res in results -%}%set line -%}        node: {{ res.node.unique_id }};status: {{ res.status }} (message: {{ res.message }})%- endset %}    {{ log(line, info=True) }}% endfor %}  {{ log("========== End Summary ==========", info=True) }}% endif %}{% endmacro %}
```

dbt_project.yml
```
on-run-end:"{{ log_results(results) }}"
```

Results:
```
12:48:17 | Concurrency: 1 threads (target='dev')12:48:17 |12:48:17 | 1 of 2 START view model dbt_jcohen.abc............................... [RUN]12:48:17 | 1 of 2 OK created view model dbt_jcohen.abc.......................... [CREATE VIEW in 0.11s]12:48:17 | 2 of 2 START table model dbt_jcohen.def.............................. [RUN]12:48:17 | 2 of 2 ERROR creating table model dbt_jcohen.def..................... [ERROR in 0.09s]12:48:17 |12:48:17 | Running 1 on-run-end hook========== Begin Summary ==========node: model.testy.abc; status: success (message: CREATE VIEW)node: model.testy.def; status: error (message: Database Error in model def (models/def.sql)  division by zero  compiled SQL at target/run/testy/models/def.sql)========== End Summary ==========12:48:17 | 1 of 1 START hook: testy.on-run-end.0................................ [RUN]12:48:17 | 1 of 1 OK hook: testy.on-run-end.0................................... [OK in 0.00s]12:48:17 |12:48:17 |12:48:17 | Finished running 1 view model, 1 table model, 1 hook in 1.94s.
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/schema ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/schema#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fschema+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fschema+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fschema+so+I+can+ask+questions+about+it.)
The schema that the model is configured to be materialized in. This is typically the same as `model['schema']`.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/selected_resources ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/selected_resources#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fselected_resources+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fselected_resources+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fselected_resources+so+I+can+ask+questions+about+it.)
On this page
The `selected_resources` context variable contains a list of all the _nodes_ selected by the current dbt command.
Currently, this variable is not accessible when using the command `run-operation`.
dbt actively builds the graph during the [parsing phase](https://docs.getdbt.com/reference/dbt-jinja-functions/execute) of running dbt projects, so the `selected_resources` context variable will be empty during parsing. Please read the information on this page to effectively use this variable.
### Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/selected_resources#usage "Direct link to Usage")
The `selected_resources` context variable is a list of all the resources selected by the current dbt command selector. Its value depends on the usage of parameters like `--select`, `--exclude` and `--selector`.
For a given run it will look like:
```
["model.my_project.model1","model.my_project.model2","snapshot.my_project.my_snapshot"]
```

Each value corresponds to a key in the `nodes` object within the [graph](https://docs.getdbt.com/reference/dbt-jinja-functions/graph) context variable.
It can be used in macros in a `pre-hook`, `post-hook`, `on-run-start` or `on-run-end` to evaluate what nodes are selected and trigger different logic whether a particular node is selected or not.
check-node-selected.sql
```
  Check if a given model is selected and trigger a different action, depending on the result{%ifexecute%}%if'model.my_project.model1'in selected_resources %}%do log("model1 is included based on the current selection", info=true)%}%else%}%do log("model1 is not included based on the current selection", info=true)%}% endif %}{% endif %}  Example output when running the code in on-run-start   when doing `dbt build`, including all nodels---------------------------------------------------------------  model1 is included based on the current selection  Example output when running the code in on-run-start   when doing `dbt run --select model2` ---------------------------------------------------------------  model1 is not included based on the current selection
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/set ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/set#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fset+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fset+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fset+so+I+can+ask+questions+about+it.)
On this page
Not to be confused with the `{% set foo = "bar" ... %}` expression in Jinja, which defines a variable. For examples of constructing SQL strings with `{% set %}` (and why `{{ }}` should not be nested inside quoted strings), see [Don’t nest your curlies](https://docs.getdbt.com/best-practices/dont-nest-your-curlies).
You can use the `set` context method to convert any iterable to a sequence of iterable elements that are unique (a set).
**Args** :
  * `value`: The iterable to convert (for example, a list)
  * `default`: A default value to return if the `value` argument is not a valid iterable


### Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/set#usage "Direct link to Usage")
```
{% set my_list = [1, 2, 2, 3] %}{% set my_set = set(my_list) %}{% do log(my_set) %}  {# {1, 2, 3} #}
```

```
{% set my_invalid_iterable = 1234 %}{% set my_set = set(my_invalid_iterable) %}{% do log(my_set) %}  {# None #}
```

```
{% set email_id = "'admin@example.com'" %}
```

### set_strict[​](https://docs.getdbt.com/reference/dbt-jinja-functions/set#set_strict "Direct link to set_strict")
The `set_strict` context method can be used to convert any iterable to a sequence of iterable elements that are unique (a set). The difference to the `set` context method is that the `set_strict` method will raise an exception on a `TypeError`, if the provided value is not a valid iterable and cannot be converted to a set.
**Args** :
  * `value`: The iterable to convert (for example, a list)


```
{% set my_list = [1, 2, 2, 3] %}{% set my_set = set(my_list) %}{% do log(my_set) %}  {# {1, 2, 3} #}
```

```
{% set my_invalid_iterable = 1234 %}{% set my_set = set_strict(my_invalid_iterable) %}{% do log(my_set) %}Compilation Error in ... (...)  'int' object is not iterable
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/run_query ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/run_query?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Frun_query+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Frun_query+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Frun_query+so+I+can+ask+questions+about+it.)
The `run_query` macro provides a convenient way to run queries and fetch their results. It is a wrapper around the [statement block](https://docs.getdbt.com/reference/dbt-jinja-functions/statement-blocks), which is more flexible, but also more complicated to use.
**Args** :
  * `sql`: The SQL query to execute


Returns a [Table](https://agate.readthedocs.io/page/api/table.html) object with the result of the query. If the specified query does not return results (eg. a DDLDML`none`.
**Note:** The `run_query` macro will not begin a transaction automatically - if you wish to run your query inside of a transaction, please use `begin` and `commit ` statements as appropriate.
Check out the section of the Getting Started guide on [using Jinja](https://docs.getdbt.com/guides/using-jinja#dynamically-retrieve-the-list-of-payment-methods) for an example of working with the results of the `run_query` macro!
**Example Usage:**
models/my_model.sql
```
{% set results = run_query('select 1 as id') %}{% if results is not none %}  {{ log(results.print_table(), info=True) }}{% endif %}{# do something with `results` here... #}
```

macros/run_grants.sql
```
{% macro run_vacuum(table) %}  {% set query %}    vacuum table {{ table }}  {% endset %}  {% do run_query(query) %}{% endmacro %}
```

Here's an example of using this (though if you're using `run_query` to return the values of a column, check out the [get_column_values](https://github.com/dbt-labs/dbt-utils#get_column_values-source) macro in the dbt-utils package).
models/my_model.sql
```
{%set payment_methods_query %}selectdistinct payment_method from app_data.paymentsorderby1{% endset %}{%set results = run_query(payment_methods_query)%}{%ifexecute%}{# Return the first column #}{%set results_list = results.columns[0].values()%}{%else%}{%set results_list =[]%}{% endif %}selectorder_id,{%for payment_method in results_list %}sum(casewhen payment_method ='{{ payment_method }}'then amount end)as {{ payment_method }}_amount,{% endfor %}sum(amount)as total_amountfrom {{ ref('raw_payments') }}groupby1
```

You can also use `run_query` to perform SQL queries that aren't select statements.
macros/run_vacuum.sql
```
{% macro run_vacuum(table)%}%set query %}    vacuum table {{ table }}% endset %}%do run_query(query)%}{% endmacro %}
```

Use the `length` filter to verify whether `run_query` returned any rows or not. Make sure to wrap the logic in an [if execute](https://docs.getdbt.com/reference/dbt-jinja-functions/execute) block to avoid unexpected behavior during parsing.
```
{%ifexecute%}{%set results = run_query(payment_methods_query)%}{%if results|length 0%}-- do something with `results` here...{%else%}-- do fallback here...{% endif %}{% endif %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/ref ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fref+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fref+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fref+so+I+can+ask+questions+about+it.)
On this page
```
select*from {{ ref("node_name") }}
```

## Definition[​](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#definition "Direct link to Definition")
This function:
  * Returns a [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) for a [model](https://docs.getdbt.com/docs/build/models), [seed](https://docs.getdbt.com/docs/build/seeds), or [snapshot](https://docs.getdbt.com/docs/build/snapshots)
  * Creates dependencies between the referenced node and the current model, which is useful for documentation and [node selection](https://docs.getdbt.com/reference/node-selection/syntax)
  * Compiles to the full object name in the database


The most important function in dbt is `ref()`; it's impossible to build even moderately complex models without it. `ref()` is how you reference one model within another. This is a very common behavior, as typically models are built to be "stacked" on top of one another. Here is how this looks in practice:
model_a.sql
```
select*frompublic.raw_data
```

model_b.sql
```
select*from {{ref('model_a')}}
```

`ref()` is, under the hood, actually doing two important things. First, it is interpolating the schema into your model file to allow you to change your deployment schema via configuration. Second, it is using these references between models to automatically build the dependency graph. This will enable dbt to deploy models in the correct order when using `dbt run`.
The `{{ ref }}` function returns a `Relation` object that has the same `table`, `schema`, and `name` attributes as the [{{ this }} variable](https://docs.getdbt.com/reference/dbt-jinja-functions/this).
## Advanced ref usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#advanced-ref-usage "Direct link to Advanced ref usage")
### Versioned ref[​](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#versioned-ref "Direct link to Versioned ref")
The `ref` function supports an optional keyword argument - `version` (or `v`). When a version argument is provided to the `ref` function, dbt returns to the `Relation` object corresponding to the specified version of the referenced model.
This functionality is useful when referencing versioned models that make breaking changes by creating new versions, but guarantees no breaking changes to existing versions of the model.
If the `version` argument is not supplied to a `ref` of a versioned model, the latest version is. This has the benefit of automatically incorporating the latest changes of a referenced model, but there is a risk of incorporating breaking changes.
#### Example[​](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#example "Direct link to Example")
models/<schema>.yml
```
models:-name: model_namelatest_version:2versions:
```

```
-- returns the `Relation` object corresponding to version 1 of model_nameselect*from {{ ref('model_name', version=1) }}
```

```
-- returns the `Relation` object corresponding to version 2 (the latest version) of model_nameselect*from {{ ref('model_name') }}
```

### Ref project-specific models[​](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#ref-project-specific-models "Direct link to Ref project-specific models")
You can also reference models from different projects using the two-argument variant of the `ref` function. By specifying both a namespace (which could be a project or package) and a model name, you ensure clarity and avoid any ambiguity in the `ref`. This is also useful when dealing with models across various projects or packages.
When using two arguments with projects (not packages), you also need to set [cross project dependencies](https://docs.getdbt.com/docs/mesh/govern/project-dependencies).
The following syntax demonstrates how to reference a model from a specific project or package:
```
select*from {{ ref('project_or_package','model_name') }}
```

We recommend using two-argument `ref` any time you are referencing a model defined in a different package or project. While not required in all cases, it's more explicit for you, for dbt, and future readers of your code.
We especially recommend using two-argument `ref` to avoid ambiguity, in cases where a model name is duplicated across multiple projects or installed packages. If you use one-argument `ref` (just the `model_name`), dbt will look for a model by that name in the same namespace (package or project); if it finds none, it will raise an error.
**Note:** The `project_or_package` should match the `name` of the project/package, as defined in its `dbt_project.yml`. This might be different from the name of the repository. It never includes the repository's organization name. For example, if you use the [`fivetran/stripe`](https://hub.getdbt.com/fivetran/stripe/latest/) package, the package name is `stripe`, not `fivetran/stripe`.
### Forcing dependencies[​](https://docs.getdbt.com/reference/dbt-jinja-functions/ref?version=1.12#forcing-dependencies "Direct link to Forcing dependencies")
In normal usage, dbt knows the proper order to run all models based on the use of the `ref` function, because it discovers them all during its parse phase. dbt will throw an error if it discovers an "unexpected" `ref` at run time (meaning it was hidden during the parsing phase). The most common cause for this is that the `ref` is inside a branch of an `if` statement that wasn't evaluated during parsing.
conditional_ref.sql
```
--This macro already has its own `if execute` check, so this one is redundant and introduced solely to cause an error{%ifexecute%}%set sql_statement %}selectmax(created_at)from {{ ref('processed_orders') }}% endset %}%-set newest_processed_order = dbt_utils.get_single_value(sql_statement,default="'2020-01-01'")-%}{% endif %}select    last_order_at '{{ newest_processed_order }}'as has_unprocessed_orderfrom {{ ref('users') }}
```

  * In this case, dbt doesn't know that `processed_orders` is a dependency because `execute` is false during parsing.
  * To address this, use a SQL comment along with the `ref` function — dbt will understand the dependency and the compiled query will still be valid:


conditional_ref.sql
```
--Now that this ref is outside of the if block, it will be detected during parsing--depends_on: {{ ref('processed_orders') }}{%ifexecute%}%set sql_statement %}selectmax(created_at)from {{ ref('processed_orders') }}% endset %}%-set newest_processed_order = dbt_utils.get_single_value(sql_statement,default="'2020-01-01'")-%}{% endif %}select    last_order_at '{{ newest_processed_order }}'as has_unprocessed_orderfrom {{ ref('users') }}
```

To ensure dbt understands the dependency, use a SQL comment instead of a Jinja comment. Jinja comments (`{# ... #}`) _don't_ work and are ignored by dbt's parser, meaning `ref` is never processed and resolved. SQL comments, however, (`--` or `/* ... */`) _do_ work because dbt still evaluates Jinja inside SQL comments.
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/target ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/target#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftarget+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftarget+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftarget+so+I+can+ask+questions+about+it.)
On this page
The `target` variable contains information about your connection to the warehouse.
  * **dbt Core :** These values are based on the target defined in your [profiles.yml](https://docs.getdbt.com/docs/local/profiles.yml) file. Please note that for certain adapters, additional configuration steps may be required. Refer to the [set up page](https://docs.getdbt.com/docs/local/connect-data-platform/about-dbt-connections) for your data platform.
  * **dbt** To learn more about setting up your adapter in dbt, refer to [About data platform connections](https://docs.getdbt.com/docs/cloud/connect-data-platform/about-connections).
    * : `target.name` is defined per job as described in [Custom target names](https://docs.getdbt.com/docs/build/custom-target-names). For other attributes, values are defined by the deployment connection. To check these values, click **Deploy** and select **Environments**. Then, select the relevant deployment environment, and click **Settings**.
    * : These values are defined by your connection and credentials. To edit these values, click on your account name in the left side menu and select **Account settings**. Then, click **Credentials**. Select and edit a project to set up the credentials and target name.


Some configurations are shared between all adapters, while others are adapter-specific. You can also use the [`--target` flag](https://docs.getdbt.com/reference/dbt-jinja-functions/target#using-the---target-flag) to set the active target when running dbt commands.
## Common[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#common "Direct link to Common")
Variable | Example | Description
---|---|---
`target.profile_name` | jaffle_shop | The name of the active profile
`target.name` | dev | Name of the active target
`target.schema` | dbt_alice | Name of the dbt schema (or, dataset on BigQuery)
`target.type` | postgres | The active adapter being used. One of "postgres", "snowflake", "bigquery", "redshift", "databricks"
`target.threads` | 4 | The number of threads in use by dbt
Loading table...
---
## Adapter-specific[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#adapter-specific "Direct link to Adapter-specific")
### Snowflake[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#snowflake "Direct link to Snowflake")
Variable | Example | Description
---|---|---
`target.database` | RAW | Database name specified in active target.
`target.warehouse` | TRANSFORM | Name of the Snowflake virtual warehouse
`target.user` | TRANSFORM_USER | The user specified in the active target
`target.role` | TRANSFORM_ROLE | The role specified in the active target
`target.account` | abc123 | The account specified in the active target
Loading table...
---
### Postgres/Redshift[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#postgresredshift "Direct link to Postgres/Redshift")
Variable | Example | Description
---|---|---
`target.dbname` | analytics | Database name specified in active target.
`target.host` | abc123.us-west-2.redshift.amazonaws.com | The host specified in active target
`target.user` | dbt_user | The user specified in the active target
`target.port` | 5439 | The port specified in the active profile
Loading table...
---
### BigQuery[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#bigquery "Direct link to BigQuery")
Variable | Example | Description
---|---|---
`target.project` | abc-123 | The project specified in the active profile
`target.dataset` | dbt_alice | The dataset the active profile
Loading table...
---
## Using the --target flag[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#using-the---target-flag "Direct link to Using the --target flag")
Use the `--target` flag when running dbt commands to set the active target and its associated `target.name` value:
```
dbt run --target dev
```

```
dbt run --target prod
```

You can use the `--target` flag with any dbt command to override the default target specified in your `profiles.yml` file. This is useful for running the same dbt project against different environments (like dev, staging, or prod) without changing your configuration files.
## Examples[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#examples "Direct link to Examples")
### Use `target.name` to limit data in dev[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#use-targetname-to-limit-data-in-dev "Direct link to use-targetname-to-limit-data-in-dev")
As long as you use sensible target names, you can perform conditional logic to limit data when working in dev.
```
selectfrom source('web_events','page_views'){%if target.name =='dev'%}where created_at >= dateadd('day',-3,current_date){% endif %}
```

### Use `target.name` to change your source database[​](https://docs.getdbt.com/reference/dbt-jinja-functions/target#use-targetname-to-change-your-source-database "Direct link to use-targetname-to-change-your-source-database")
If you have specific Snowflake databases configured for your dev/qa/prod environments, you can set up your sources to compile to different databases depending on your environment.
```
sources:-name: source_name database:|      {%- if  target.name == "dev" -%} raw_dev      {%- elif target.name == "qa"  -%} raw_qa      {%- elif target.name == "prod"  -%} raw_prod      {%- else -%} invalid_database      {%- endif -%}schema: source_schema
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/schemas ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/schemas#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fschemas+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fschemas+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fschemas+so+I+can+ask+questions+about+it.)
`schemas` is a variable available in an `on-run-end` hook, representing a list of schemas that dbt built objects in on this run.
If you do not use [custom schemas](https://docs.getdbt.com/docs/build/custom-schemas), `schemas` will evaluate to your target schema, e.g. `['dbt_alice']`. If you use custom schemas, it will include these as well, e.g. `['dbt_alice', 'dbt_alice_marketing', 'dbt_alice_finance']`.
The `schemas` variable is useful for granting privileges to all schemas that dbt builds relations in, like so (note this is Redshift specific syntax):
dbt_project.yml
```
on-run-end:-"{% for schema in schemas%}grant usage on schema {{ schema }} to group reporter;{% endfor%}"-"{% for schema in schemas %}grant select on all tables in schema {{ schema }} to group reporter;{% endfor%}"-"{% for schema in schemas %}alter default privileges in schema {{ schema }}  grant select on tables to group reporter;{% endfor %}"
```

We've written a full discourse article [here](https://discourse.getdbt.com/t/the-exact-grant-statements-we-use-in-a-dbt-project/430)
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/this ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/this#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fthis+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fthis+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fthis+so+I+can+ask+questions+about+it.)
On this page
`this` is the database representation of the current model. It is useful when:
  * Defining a `where` statement within [incremental models](https://docs.getdbt.com/docs/build/incremental-models)
  * Using [pre or post hooks](https://docs.getdbt.com/reference/resource-configs/pre-hook-post-hook)


`this` is a [Relation](https://docs.getdbt.com/reference/dbt-classes#relation), and as such, properties such as `{{ this.database }}` and `{{ this.schema }}` compile as expected.
  * Note — Prior to dbt v1.6, returns `request` as the result of `{{ ref.identifier }}`.


`this` can be thought of as equivalent to `ref('<the_current_model>')`, and is a neat way to avoid circular dependencies.
## Examples[​](https://docs.getdbt.com/reference/dbt-jinja-functions/this#examples "Direct link to Examples")
### Configuring incremental models[​](https://docs.getdbt.com/reference/dbt-jinja-functions/this#configuring-incremental-models "Direct link to Configuring incremental models")
models/stg_events.sql
```
{{ config(materialized='incremental') }}select    my_slow_function(my_column)from raw_app_data.events{%if is_incremental()%}where event_time (selectmax(event_time)from {{ this }}){% endif %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/statement-blocks ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/statement-blocks#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fstatement-blocks+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fstatement-blocks+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fstatement-blocks+so+I+can+ask+questions+about+it.)
We recommend using the [`run_query` macro](https://docs.getdbt.com/reference/dbt-jinja-functions/run_query) instead of `statement` blocks. The `run_query` macro provides a more convenient way to run queries and fetch their results by wrapping `statement` blocks. You can use this macro to write more concise code that is easier to maintain.
`statement`s are SQL queries that hit the database and return results to your Jinja context. Here’s an example of a `statement` which gets all of the states from a users table.
get_states_statement.sql
```
-- depends_on: {{ ref('users') }}{%-call statement('states', fetch_result=True)-%}selectdistinct state from {{ ref('users') }}{%- endcall -%}
```

The signature of the `statement` block looks like this:
```
statement(name=None, fetch_result=False, auto_begin=True)
```

When executing a `statement`, dbt needs to understand how to resolve references to other dbt models or resources. If you are already `ref`ing the model outside of the statement block, the dependency will be automatically inferred, but otherwise you will need to [force the dependency](https://docs.getdbt.com/reference/dbt-jinja-functions/ref#forcing-dependencies) with `-- depends_on`.
Example using -- depends_on
```
-- depends_on: {{ ref('users') }}{%call statement('states', fetch_result=True)-%}selectdistinct state from {{ ref('users') }}    The unique states are: {{ load_result('states')['data'] }}{%- endcall %}
```

Example using ref() function
```
{%call statement('states', fetch_result=True)-%}selectdistinct state from {{ ref('users') }}    The unique states are: {{ load_result('states')['data'] }}{%- endcall %}select id *2from {{ ref('users') }}
```

**Args** :
  * `name` (string): The name for the result set returned by this statement
  * `fetch_result` (bool): If True, load the results of the statement into the Jinja context
  * `auto_begin` (bool): If True, open a transaction if one does not exist. If false, do not open a transaction.


Once the statement block has executed, the result set is accessible via the `load_result` function. The result object includes three keys:
  * `response`: Structured object containing metadata returned from the database, which varies by adapter. E.g. success `code`, number of `rows_affected`, total `bytes_processed`, etc. Comparable to `adapter_response` in the [Result object](https://docs.getdbt.com/reference/dbt-classes#result-objects).
  * `data`: Pythonic representation of data returned by query (arrays, tuples, dictionaries).
  * `table`: [Agate](https://agate.readthedocs.io/page/api/table.html) table representation of data returned by query.


For the above statement, that could look like:
load_states.sql
```
{%-set states = load_result('states')-%}{%-set states_data = states['data']-%}{%-set states_status = states['response']-%}
```

The contents of the returned `data` field is a matrix. It contains a list rows, with each row being a list of values returned by the database. For the above example, this data structure might look like:
states.sql
```
 log(states_data)['PA'],['NY'],['CA'],
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/thread_id ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/thread_id#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fthread_id+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fthread_id+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fthread_id+so+I+can+ask+questions+about+it.)
The `thread_id` outputs an identifier for the current Python thread that is executing a node, like `Thread-1`.
This value is useful when auditing or analyzing dbt invocation metadata. It corresponds to the `thread_id` within the [`Result` object](https://docs.getdbt.com/reference/dbt-classes#result-objects) and [`run_results.json`](https://docs.getdbt.com/reference/artifacts/run-results-json).
If available, the `thread_id` is:
  * available in the compilation context of [`query-comment`](https://docs.getdbt.com/reference/project-configs/query-comment)
  * included in the `info` dictionary in dbt [events and logs](https://docs.getdbt.com/reference/events-logging#info)
  * included in the `metadata` dictionary in [dbt artifacts](https://docs.getdbt.com/reference/artifacts/dbt-artifacts#common-metadata)
  * included as a label in all BigQuery jobs that dbt originates


## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/source ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/source#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fsource+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fsource+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fsource+so+I+can+ask+questions+about+it.)
On this page
```
select*from {{ source("source_name","table_name") }}
```

## Definition[​](https://docs.getdbt.com/reference/dbt-jinja-functions/source#definition "Direct link to Definition")
This function:
  * Returns a [Relation](https://docs.getdbt.com/reference/dbt-classes#relation) for a [source](https://docs.getdbt.com/docs/build/sources)
  * Creates dependencies between a source and the current model, which is useful for documentation and [node selection](https://docs.getdbt.com/reference/node-selection/syntax)
  * Compiles to the full object name in the database


## Related guides[​](https://docs.getdbt.com/reference/dbt-jinja-functions/source#related-guides "Direct link to Related guides")


## Arguments[​](https://docs.getdbt.com/reference/dbt-jinja-functions/source#arguments "Direct link to Arguments")
  * `source_name`: The `name:` defined under a `sources:` key
  * `table_name`: The `name:` defined under a `tables:` key


## Example[​](https://docs.getdbt.com/reference/dbt-jinja-functions/source#example "Direct link to Example")
Consider a source defined as follows:
models/<filename>.yml
```
sources:-name: jaffle_shop # this is the source_namedatabase: rawtables:-name: customers # this is the table_name-name: orders
```

Select from the source in a model:
models/orders.sql
```
selectfrom {{ source('jaffle_shop','customers') }}leftjoin {{ source('jaffle_shop','orders') }} using(customer_id)
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/tojson ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/tojson?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftojson+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftojson+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftojson+so+I+can+ask+questions+about+it.)
On this page
The `tojson` context method can be used to serialize a Python object primitive, eg. a `dict` or `list` to a JSON string.
**Args** :
  * `value`: The value to serialize to JSON (required)
  * `default`: A default value to return if the `value` argument cannot be serialized (optional)


### Usage:[​](https://docs.getdbt.com/reference/dbt-jinja-functions/tojson?version=1.12#usage "Direct link to Usage:")
```
{% set my_dict = {"abc": 123} %}{% set my_json_string = tojson(my_dict) %}{% do log(my_json_string) %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/toyaml ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/toyaml#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftoyaml+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftoyaml+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Ftoyaml+so+I+can+ask+questions+about+it.)
On this page
The `toyaml` context method can be used to serialize a Python object primitive, eg. a `dict` or `list` to a YAML string.
**Args** :
  * `value`: The value to serialize to YAML (required)
  * `default`: A default value to return if the `value` argument cannot be serialized (optional)


### Usage:[​](https://docs.getdbt.com/reference/dbt-jinja-functions/toyaml#usage "Direct link to Usage:")
```
{% set my_dict = {"abc": 123} %}{% set my_yaml_string = toyaml(my_dict) %}{% do log(my_yaml_string) %}
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/zip ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/zip#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fzip+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fzip+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fzip+so+I+can+ask+questions+about+it.)
On this page
The `zip` context method can be used to return an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument iterables. For more information, see [Python docs](https://docs.python.org/3/library/functions.html#zip).
**Args** :
  * `*args`: Any number of iterables
  * `default`: A default value to return if `*args` is not iterable


### Usage[​](https://docs.getdbt.com/reference/dbt-jinja-functions/zip#usage "Direct link to Usage")
```
{% set my_list_a = [1, 2] %}{% set my_list_b = ['alice', 'bob'] %}{% set my_zip = zip(my_list_a, my_list_b) | list %}{% do log(my_zip) %}  {# [(1, 'alice'), (2, 'bob')] #}
```

```
{% set my_list_a = 12 %}{% set my_list_b = ['alice', 'bob'] %}{% set my_zip = zip(my_list_a, my_list_b, default = []) | list %}{% do log(my_zip) %}  {# [] #}
```

### zip_strict[​](https://docs.getdbt.com/reference/dbt-jinja-functions/zip#zip_strict "Direct link to zip_strict")
The `zip_strict` context method can be used to used to return an iterator of tuples, just like `zip`. The difference to the `zip` context method is that the `zip_strict` method will raise an exception on a `TypeError`, if one of the provided values is not a valid iterable.
**Args** :
  * `value`: The iterable to convert (e.g. a list)


```
{% set my_list_a = [1, 2] %}{% set my_list_b = ['alice', 'bob'] %}{% set my_zip = zip_strict(my_list_a, my_list_b) | list %}{% do log(my_zip) %}  {# [(1, 'alice'), (2, 'bob')] #}
```

```
{% set my_list_a = 12 %}{% set my_list_b = ['alice', 'bob'] %}{% set my_zip = zip_strict(my_list_a, my_list_b) %}Compilation Error in ... (...)  'int' object is not iterable
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbt-jinja-functions/var ---

[Skip to main content](https://docs.getdbt.com/reference/dbt-jinja-functions/var#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fvar+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fvar+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbt-jinja-functions%2Fvar+so+I+can+ask+questions+about+it.)
On this page
To retrieve a variable inside a model, hook, or macro, use the `var()` function. The `var()` function returns the value defined in your project or passed using `--vars`, based on precedence.
You can use `var()` anywhere dbt renders Jinja during compilation, including most `.sql` and `.yml` files in your project. It does not work in configuration files that dbt reads before compilation, such as [`profiles.yml`](https://docs.getdbt.com/reference/dbt-jinja-functions/profiles-yml-context) or [`packages.yml`](https://docs.getdbt.com/reference/dbt-jinja-functions/packages.yml%20context).
To add a variable to a model, use the `var()` function:
my_model.sql
```
select*from events where event_type ='{{ var("event_type") }}'
```

If you try to run this model without supplying an `event_type` variable, you'll receive a compilation error that looks like this:
```
Encountered an error:! Compilation error while compiling model package_name.my_model:! Required var 'event_type' not found in config:Vars supplied to package_name.my_model = {
```

### Variable default values[​](https://docs.getdbt.com/reference/dbt-jinja-functions/var#variable-default-values "Direct link to Variable default values")
The `var()` function takes an optional second argument, `default`. If this argument is provided, then it will be the default value for the variable if one is not explicitly defined.
my_model.sql
```
-- Use 'activation' as the event_type if the variable is not defined.select*from events where event_type ='{{ var("event_type", "activation") }}'
```

### Command line variables[​](https://docs.getdbt.com/reference/dbt-jinja-functions/var#command-line-variables "Direct link to Command line variables")
The `dbt_project.yml` file is a great place to define variables that rarely change.
When you need to override a variable for a specific run, use the `--vars` command line option. For example, when you want to test with a different date range, run models with environment-specific settings, or adjust behavior dynamically.
Use `--vars` to pass one or more variables to a dbt command. Provide the argument as a YAML dictionary string.
For example:
```
$ dbt run --vars '{"event_type": "signup"}'
```

Inside a model or macro, access the value using the `var()` function:
```
select '{{ var("event_type") }}' as event_type
```

When you pass variables using `--vars`, you can access them anywhere you use the `var()` function in your project.
You can pass multiple variables at once:
```
$ dbt run --vars '{event_type: signup, region: us}'
```

If only one variable is being set, the brackets are optional:
```
$ dbt run --vars 'event_type: signup'
```

The `--vars` argument accepts a YAML dictionary as a string on the command line. YAML is convenient because it does not require strict quoting as with JSON.
Both of the following are valid and equivalent:
```
$ dbt run --vars '{"key": "value", "date": 20180101}'$ dbt run --vars '{key: value, date: 20180101}'
```

Variables defined using `--var`, override values defined in `dbt_project.yml`. This makes `--vars` useful for temporarily overriding configuration without changing your committed project files. For the complete order of precedence (including package-scoped variables and default values defined in `var()`), see [Variable precedence](https://docs.getdbt.com/docs/build/project-variables#variable-precedence).
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/dbtignore ---

[Skip to main content](https://docs.getdbt.com/reference/dbtignore#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbtignore+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbtignore+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdbtignore+so+I+can+ask+questions+about+it.)
You can create a `.dbtignore` file in the root of your [dbt project](https://docs.getdbt.com/docs/build/projects) to specify files that should be **entirely** ignored by dbt. The file behaves like a [`.gitignore` file, using the same syntax](https://git-scm.com/docs/gitignore). Files and subdirectories matching the pattern will not be read, parsed, or otherwise detected by dbt—as if they didn't exist.
**Examples**
.dbtignore
```
# .dbtignore# ignore individual .py filesnot-a-dbt-model.pyanother-non-dbt-model.py# ignore all .py files**.py# ignore all .py files with "codegen" in the filename*codegen*.py# ignore all folders in a directorypath/to/folders/**# ignore some folders in a directorypath/to/folders/subfolder/**
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/define-configs ---

[Skip to main content](https://docs.getdbt.com/reference/define-configs#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdefine-configs+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdefine-configs+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdefine-configs+so+I+can+ask+questions+about+it.)
On this page
Learn how to define configurations for your resources in a dbt project
Depending on the resource type, you can define configurations in a dbt project and also in an installed package by:
## Config inheritance[​](https://docs.getdbt.com/reference/define-configs#config-inheritance "Direct link to Config inheritance")
The most specific config always takes precedence. This generally follows the order above: an in-file `config()` block --> properties defined in a `.yml` file --> config defined in the project file.
Note - Generic data tests work a little differently when it comes to specificity. See [test configs](https://docs.getdbt.com/reference/data-test-configs).
Within the project file, configurations are also applied hierarchically. The most specific config always takes precedence. In the project file, for example, configurations applied to a `marketing` subdirectory will take precedence over configurations applied to the entire `jaffle_shop` project. To apply a configuration to a model or directory of models, define the [resource path](https://docs.getdbt.com/reference/resource-configs/resource-path) as nested dictionary keys.
Configurations in your root dbt project have _higher_ precedence than configurations in installed packages. This enables you to override the configurations of installed packages, providing more control over your dbt runs.
## Combining configs[​](https://docs.getdbt.com/reference/define-configs#combining-configs "Direct link to Combining configs")
Most configurations are "clobbered" when applied hierarchically. Whenever a more specific value is available, it will completely replace the less specific value. Note that a few configs have different merge behavior:
  * [`tags`](https://docs.getdbt.com/reference/resource-configs/tags) are additive. If a model has some tags configured in `dbt_project.yml`, and more tags are applied in its `.sql` file, the final set of tags will include all of them.
  * [`meta`](https://docs.getdbt.com/reference/resource-configs/meta) dictionaries are merged (a more specific key-value pair replaces a less specific value with the same key).
  * When using the [`freshness`](https://docs.getdbt.com/reference/resource-configs/freshness) config, a more specific key-value pair replaces a less specific value with the same key.
  * [`pre-hook` and `post-hook`](https://docs.getdbt.com/reference/resource-configs/pre-hook-post-hook) are also additive.
  * For clobbering and merging configurations that are inherited from multiple levels, the general rules are:
    * Node-level configs (more specific) clobber project-level configs (less specific).
    * For sources, table-level configs (more specific) clobber source-level configs (less specific).
    * The root project's configuration in `dbt_project.yml` clobbers configuration within package files. This is so that users can control the behavior of packages they are installing using `dbt deps` without needing to edit the code in those package files directly.


## The `+` prefix[​](https://docs.getdbt.com/reference/define-configs#the--prefix "Direct link to the--prefix")
dbt demarcates between a folder name and a configuration by using a `+` prefix before the configuration name. The `+` prefix is used for configs _only_ and applies to `dbt_project.yml` under the corresponding resource key. It doesn't apply to:
  * `config()` Jinja macro within a resource file
  * config property in a `.yml` file.


For more info, see the [Using the `+` prefix](https://docs.getdbt.com/reference/resource-configs/plus-prefix).
## Example[​](https://docs.getdbt.com/reference/define-configs#example "Direct link to Example")
Here's an example that defines both `sources` and `models` for a project:
models/jaffle_shop.yml
```
version:2sources:-name: raw_jaffle_shopdescription: A replica of the postgres database used to power the jaffle_shop app.tables:-name: customerscolumns:-name: iddescription: Primary key of the tabledata_tests:- unique- not_null-name: orderscolumns:-name: iddescription: Primary key of the tabledata_tests:- unique- not_null-name: user_iddescription: Foreign key to customers-name: statusdata_tests:-accepted_values:arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.values:['placed','shipped','completed','return_pending','returned']models:-name: stg_jaffle_shop__customers #  Must match the filename of a model -- including case sensitivity.config:tags:['pii']columns:-name: customer_iddata_tests:- unique- not_null-name: stg_jaffle_shop__ordersconfig:materialized: viewcolumns:-name: order_iddata_tests:- unique- not_null-name: statusdata_tests:-accepted_values:arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.values:['placed','shipped','completed','return_pending','returned']config:severity: warn
```

## Related documentation[​](https://docs.getdbt.com/reference/define-configs#related-documentation "Direct link to Related documentation")
You can find an exhaustive list of each supported property and config, broken down by resource type:
  * Model [properties](https://docs.getdbt.com/reference/model-properties) and [configs](https://docs.getdbt.com/reference/model-configs)
  * Source [properties](https://docs.getdbt.com/reference/source-properties) and [configs](https://docs.getdbt.com/reference/source-configs)
  * Seed [properties](https://docs.getdbt.com/reference/seed-properties) and [configs](https://docs.getdbt.com/reference/seed-configs)
  * Snapshot [properties](https://docs.getdbt.com/reference/snapshot-properties)
  * Analysis [properties](https://docs.getdbt.com/reference/analysis-properties)
  * Macro [properties](https://docs.getdbt.com/reference/macro-properties)
  * Exposure [properties](https://docs.getdbt.com/reference/exposure-properties)


## FAQs[​](https://docs.getdbt.com/reference/define-configs#faqs "Direct link to FAQs")
Does my `.yml` file containing tests and descriptions need to be named `schema.yml`?
No! You can name this file whatever you want (including `whatever_you_want.yml`), so long as:
  * The file is in your `models/` directory¹
  * The file has `.yml` extension


Check out the [docs](https://docs.getdbt.com/reference/configs-and-properties) for more information.
¹If you're declaring properties for seeds, snapshots, or macros, you can also place this file in the related directory — `seeds/`, `snapshots/` and `macros/` respectively.
If I can name these files whatever I'd like, what should I name them?
It's up to you! Here's a few options:
  * Default to the existing terminology: `schema.yml` (though this does make it hard to find the right file over time)
  * Use the same name as your directory (assuming you're using sensible names for your directories)
  * If you test and document one model (or seed, snapshot, macro etc.) per file, you can give it the same name as the model (or seed, snapshot, macro etc.)


Choose what works for your team. We have more recommendations in our guide on [structuring dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview).
Should I use separate files to declare resource properties, or one large file?
It's up to you:
  * Some folks find it useful to have one file per model (or source / snapshot / seed etc)
  * Some find it useful to have one per directory, documenting and testing multiple models in one file


Choose what works for your team. We have more recommendations in our guide on [structuring dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview).
Can I add tests and descriptions in a SQL config block?
dbt has the ability to define node configs in YAML files, in addition to `config()` blocks and `dbt_project.yml`. But the reverse isn't always true: there are some things in `.yml` files that can _only_ be defined there.
Certain properties are special, because:
  * They have a unique Jinja rendering context
  * They create new project resources
  * They don't make sense as hierarchical configuration
  * They're older properties that haven't yet been redefined as configs


These properties are:
  * `columns`
  * [`source` properties](https://docs.getdbt.com/reference/source-properties) (e.g. `loaded_at_field`, `freshness`)
  * [`exposure` properties](https://docs.getdbt.com/reference/exposure-properties) (e.g. `type`, `maturity`)
  * [`macro` properties](https://docs.getdbt.com/reference/resource-properties/arguments) (e.g. `arguments`)


Why do model and source YAML files always start with `version: 2`?
Once upon a time, the structure of these `.yml` files was very different (s/o to anyone who was using dbt back then!). Adding `version: 2` allowed us to make this structure more extensible.
From [dbt Core v1.5](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older%20versions/upgrading-to-v1.5#quick-hits), the top-level `version:` key is optional in all resource YAML files. If present, only `version: 2` is supported.
Also starting in v1.5, both the [`config-version: 2`](https://docs.getdbt.com/reference/project-configs/config-version) and the top-level `version:` key in the `dbt_project.yml` are optional.
Resource YAML files do not currently require this config. We only support `version: 2` if it's specified. Although we do not expect to update YAML files to `version: 3` soon, having this config will make it easier for us to introduce new structures in the future
Can I use a YAML file extension?
No. At present, dbt will only search for files with a `.yml` file extension. In a future release of dbt, dbt will also search for files with a `.yaml` file extension.
## Troubleshooting common errors[​](https://docs.getdbt.com/reference/define-configs#troubleshooting-common-errors "Direct link to Troubleshooting common errors")
Invalid test config given in [model name]
This error occurs when your `.yml` file does not conform to the structure expected by dbt. A full error message might look like:
```
* Invalid test config given in models/schema.yml near {'namee': 'event', ...}  Invalid arguments passed to "UnparsedNodeUpdate" instance: 'name' is a required property, Additional properties are not allowed ('namee' was unexpected)
```

While verbose, an error like this should help you track down the issue. Here, the `name` field was provided as `namee` by accident. To fix this error, ensure that your `.yml` conforms to the expected structure described in this guide.
Invalid syntax in your schema.yml file
If your `.yml` file is not valid yaml, then dbt will show you an error like this:
```
Runtime Error  Syntax error near line 6  ------------------------------  5  |   - name: events  6  |     description; "A table containing clickstream events from the marketing website"  7  |  Raw Error:  ------------------------------  while scanning a simple key    in "<unicode string>", line 6, column 5:          description; "A table containing clickstream events from the marketing website"
```

This error occurred because a semicolon (`;`) was accidentally used instead of a colon (`:`) after the `description` field. To resolve issues like this, find the `.yml` file referenced in the error message and fix any syntax errors present in the file. There are online YAML validators that can be helpful here, but please be mindful of submitting sensitive information to third-party applications!
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/define-properties ---

[Skip to main content](https://docs.getdbt.com/reference/define-properties?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdefine-properties+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdefine-properties+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fdefine-properties+so+I+can+ask+questions+about+it.)
On this page
Learn how to define properties for your resources in a properties.yml file
In dbt, you can use `properties.yml` files to define properties for resources. You can declare properties in `.yml` files, in the same directory as your resources. You can name these files `whatever_you_want.yml` and nest them arbitrarily in sub-folders within each directory.
We highly recommend that you define properties in dedicated paths alongside the resources they're describing.
#### schema.yml files[​](https://docs.getdbt.com/reference/define-properties?version=1.12#schemayml-files "Direct link to schema.yml files")
Previous versions of the docs referred to these as `schema.yml` files — we've moved away from that terminology since the word `schema` is used to mean other things when talking about databases, and people often thought that you _had_ to name these files `schema.yml`.
Instead, we now refer to these files as `properties.yml` files. (Of course, you're still free to name your files `schema.yml`)
### Which properties are _not_ also configs?[​](https://docs.getdbt.com/reference/define-properties?version=1.12#which-properties-are-not-also-configs "Direct link to which-properties-are-not-also-configs")
In dbt, you can define node configs in `properties.yml` files, in addition to `config()` blocks and `dbt_project.yml`. However, some special properties can only be defined in the `.yml` file and you cannot configure them using `config()` blocks or the `dbt_project.yml` file:
Certain properties are special, because:
  * They have a unique Jinja rendering context
  * They create new project resources
  * They don't make sense as hierarchical configuration
  * They're older properties that haven't yet been redefined as configs


These properties are:
  * [`source` properties](https://docs.getdbt.com/reference/source-properties) (for example, `loaded_at_field`)
  * [`exposure` properties](https://docs.getdbt.com/reference/exposure-properties) (for example, `type`, `maturity`)
    * Note that while most exposure properties must be configured directly in `properties.yml` files, you can set the [`enabled`](https://docs.getdbt.com/reference/resource-configs/enabled) config at the [project level](https://docs.getdbt.com/reference/exposure-properties#project-level-configs) in the`dbt_project.yml` file.
  * [`macro` properties](https://docs.getdbt.com/reference/macro-properties) (for example, `arguments`)


## Example[​](https://docs.getdbt.com/reference/define-properties?version=1.12#example "Direct link to Example")
Here's an example that defines both `sources` and `models` for a project:
models/jaffle_shop.yml
```
version:2sources:-name: raw_jaffle_shopdescription: A replica of the postgres database used to power the jaffle_shop app.tables:-name: customerscolumns:-name: iddescription: Primary key of the tabledata_tests:- unique- not_null-name: orderscolumns:-name: iddescription: Primary key of the tabledata_tests:- unique- not_null-name: user_iddescription: Foreign key to customers-name: statusdata_tests:-accepted_values:arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.values:['placed','shipped','completed','return_pending','returned']models:-name: stg_jaffle_shop__customers #  Must match the filename of a model -- including case sensitivity.config:tags:['pii']columns:-name: customer_iddata_tests:- unique- not_null-name: stg_jaffle_shop__ordersconfig:materialized: viewcolumns:-name: order_iddata_tests:- unique- not_null-name: statusdata_tests:-accepted_values:arguments:# available in v1.10.5 and higher. Older versions can set the <argument_name> as the top-level property.values:['placed','shipped','completed','return_pending','returned']config:severity: warn
```

## Related documentation[​](https://docs.getdbt.com/reference/define-properties?version=1.12#related-documentation "Direct link to Related documentation")
You can find an exhaustive list of each supported property and config, broken down by resource type:
  * Model [properties](https://docs.getdbt.com/reference/model-properties) and [configs](https://docs.getdbt.com/reference/model-configs)
  * Source [properties](https://docs.getdbt.com/reference/source-properties) and [configs](https://docs.getdbt.com/reference/source-configs)
  * Seed [properties](https://docs.getdbt.com/reference/seed-properties) and [configs](https://docs.getdbt.com/reference/seed-configs)
  * Snapshot [properties](https://docs.getdbt.com/reference/snapshot-properties)
  * Analysis [properties](https://docs.getdbt.com/reference/analysis-properties)
  * Macro [properties](https://docs.getdbt.com/reference/macro-properties)
  * Exposure [properties](https://docs.getdbt.com/reference/exposure-properties)


## FAQs[​](https://docs.getdbt.com/reference/define-properties?version=1.12#faqs "Direct link to FAQs")
Does my `.yml` file containing tests and descriptions need to be named `schema.yml`?
No! You can name this file whatever you want (including `whatever_you_want.yml`), so long as:
  * The file is in your `models/` directory¹
  * The file has `.yml` extension


Check out the [docs](https://docs.getdbt.com/reference/configs-and-properties) for more information.
¹If you're declaring properties for seeds, snapshots, or macros, you can also place this file in the related directory — `seeds/`, `snapshots/` and `macros/` respectively.
If I can name these files whatever I'd like, what should I name them?
It's up to you! Here's a few options:
  * Default to the existing terminology: `schema.yml` (though this does make it hard to find the right file over time)
  * Use the same name as your directory (assuming you're using sensible names for your directories)
  * If you test and document one model (or seed, snapshot, macro etc.) per file, you can give it the same name as the model (or seed, snapshot, macro etc.)


Choose what works for your team. We have more recommendations in our guide on [structuring dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview).
Should I use separate files to declare resource properties, or one large file?
It's up to you:
  * Some folks find it useful to have one file per model (or source / snapshot / seed etc)
  * Some find it useful to have one per directory, documenting and testing multiple models in one file


Choose what works for your team. We have more recommendations in our guide on [structuring dbt projects](https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview).
Can I add tests and descriptions in a SQL config block?
dbt has the ability to define node configs in YAML files, in addition to `config()` blocks and `dbt_project.yml`. But the reverse isn't always true: there are some things in `.yml` files that can _only_ be defined there.
Certain properties are special, because:
  * They have a unique Jinja rendering context
  * They create new project resources
  * They don't make sense as hierarchical configuration
  * They're older properties that haven't yet been redefined as configs


These properties are:
  * `columns`
  * [`source` properties](https://docs.getdbt.com/reference/source-properties) (e.g. `loaded_at_field`, `freshness`)
  * [`exposure` properties](https://docs.getdbt.com/reference/exposure-properties) (e.g. `type`, `maturity`)
  * [`macro` properties](https://docs.getdbt.com/reference/resource-properties/arguments) (e.g. `arguments`)


Why do model and source YAML files always start with `version: 2`?
Once upon a time, the structure of these `.yml` files was very different (s/o to anyone who was using dbt back then!). Adding `version: 2` allowed us to make this structure more extensible.
From [dbt Core v1.5](https://docs.getdbt.com/docs/dbt-versions/core-upgrade/Older%20versions/upgrading-to-v1.5#quick-hits), the top-level `version:` key is optional in all resource YAML files. If present, only `version: 2` is supported.
Also starting in v1.5, both the [`config-version: 2`](https://docs.getdbt.com/reference/project-configs/config-version) and the top-level `version:` key in the `dbt_project.yml` are optional.
Resource YAML files do not currently require this config. We only support `version: 2` if it's specified. Although we do not expect to update YAML files to `version: 3` soon, having this config will make it easier for us to introduce new structures in the future
Can I use a YAML file extension?
No. At present, dbt will only search for files with a `.yml` file extension. In a future release of dbt, dbt will also search for files with a `.yaml` file extension.
## Troubleshooting common errors[​](https://docs.getdbt.com/reference/define-properties?version=1.12#troubleshooting-common-errors "Direct link to Troubleshooting common errors")
Invalid test config given in [model name]
This error occurs when your `.yml` file does not conform to the structure expected by dbt. A full error message might look like:
```
* Invalid test config given in models/schema.yml near {'namee': 'event', ...}  Invalid arguments passed to "UnparsedNodeUpdate" instance: 'name' is a required property, Additional properties are not allowed ('namee' was unexpected)
```

While verbose, an error like this should help you track down the issue. Here, the `name` field was provided as `namee` by accident. To fix this error, ensure that your `.yml` conforms to the expected structure described in this guide.
Invalid syntax in your schema.yml file
If your `.yml` file is not valid yaml, then dbt will show you an error like this:
```
Runtime Error  Syntax error near line 6  ------------------------------  5  |   - name: events  6  |     description; "A table containing clickstream events from the marketing website"  7  |  Raw Error:  ------------------------------  while scanning a simple key    in "<unicode string>", line 6, column 5:          description; "A table containing clickstream events from the marketing website"
```

This error occurred because a semicolon (`;`) was accidentally used instead of a colon (`:`) after the `description` field. To resolve issues like this, find the `.yml` file referenced in the error message and fix any syntax errors present in the file. There are online YAML validators that can be helpful here, but please be mindful of submitting sensitive information to third-party applications!
## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/model-properties ---

[Skip to main content](https://docs.getdbt.com/reference/model-properties#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fmodel-properties+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fmodel-properties+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fmodel-properties+so+I+can+ask+questions+about+it.)
On this page
Models properties can be declared in `.yml` files in your `models/` directory (as defined by the [`model-paths` config](https://docs.getdbt.com/reference/project-configs/model-paths)).
You can name these files `whatever_you_want.yml`, and nest them arbitrarily deeply in subfolders within the `models/` directory.
## Available top-level model properties[​](https://docs.getdbt.com/reference/model-properties#available-top-level-model-properties "Direct link to Available top-level model properties")
Property | Type | Required | Description
---|---|---|---
string | Yes | The model name (must match the model filename).
string | No | Documentation for the model.
array | No | List of column definitions.
object | No | Model configuration (materialization, tags, etc.).
array | No | Model-level constraints (primary key, foreign key, etc.).
array | No | Model-level data tests.
tests | array | No | Legacy alias for data_tests.
array | No | Model version definitions.
string/float | No | The latest version of the model.
string | No | Date when the model is deprecated.
string | No | Access level: private, protected, or public. Supported at the top-level for backwards compatibility only.
object | No | Time spine configuration for semantic layer.
Loading table...
---
### Example file[​](https://docs.getdbt.com/reference/model-properties#example-file "Direct link to Example file")
models/<filename>.yml
```
models:# Model name must match the filename of a model -- including case sensitivity: model_name: <markdown_string>: <version_identifier>: <YAML_DateTime>:: <config_value>show: true | falsenode_color: <color_id# Use name (such as node_color: purple) or hex code with quotes (such as node_color: "#cd7f32"): private | protected | public:- <constraint:- <test-...# declare additional data tests:-name: <column_name# required: <markdown_string>: true | false:- <constraint:- <test-...# declare additional data tests:: {<dictionary>}: [<string>]# only required in conjunction with time_spine key: <any supported time granularity[](https://docs.getdbt.com/docs/build/dimensions?dimension=time_gran)-name:...# declare properties of additional columns:standard_granularity_column: <column_name:: <version_identifier> # required: <definition_file_name>: <markdown_string>:- <constraint:: <config_value>show: true | false: private | protected | public:- <test-...# declare additional data testscolumns:# include/exclude columns from the top-level model properties: <include_value>: <exclude_list># specify additional columns-name: <column_name# required: true | false:- <constraint:- <test-...# declare additional data tests: [<string>]-v:...# declare additional versions
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/exposure-properties ---

[Skip to main content](https://docs.getdbt.com/reference/exposure-properties?version=1.12#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fexposure-properties+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fexposure-properties+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fexposure-properties+so+I+can+ask+questions+about+it.)
On this page
## Related documentation[​](https://docs.getdbt.com/reference/exposure-properties?version=1.12#related-documentation "Direct link to Related documentation")
  * [Using exposures](https://docs.getdbt.com/docs/build/exposures)
  * [Declaring resource properties](https://docs.getdbt.com/reference/configs-and-properties)


## Overview[​](https://docs.getdbt.com/reference/exposure-properties?version=1.12#overview "Direct link to Overview")
Exposures are defined in `properties.yml` files nested under an `exposures:` key. You may define `exposures` in YAML files that also define `sources` or `models`. Exposure properties are "special properties" in that you can't configure them in the `dbt_project.yml` file or using `config()` blocks. Refer to [ Configs and properties](https://docs.getdbt.com/reference/define-properties#which-properties-are-not-also-configs) for more info.
Note that while most exposure properties must be configured directly in these YAML files, you can set the [`enabled`](https://docs.getdbt.com/reference/resource-configs/enabled) config at the [project level](https://docs.getdbt.com/reference/exposure-properties?version=1.12#project-level-configs) in the`dbt_project.yml` file.
You can name these files `whatever_you_want.yml`, and nest them arbitrarily deeply in subfolders within the `models/` directory.
Exposure names must contain only letters, numbers, and underscores (no spaces or special characters). For a short human-friendly name with title casing, spaces, and special characters, use the `label` property.
models/<filename>.yml
```
exposures:-name: <string_with_underscores: <markdown_string>type:{dashboard, notebook, analysis, ml, application}url: <stringmaturity:{high, medium, low}# Indicates level of confidence or stability in the exposure: true | false: # 'tags' and 'meta' changed to config in v1.10: [<string>] : {<dictionary>}enabled: true | falseowner:# supports 'name' and 'email' onlyname: <stringemail: <stringdepends_on:- ref('model')- ref('seed')- source('name', 'table')- metric('metric_name')label:"Human-Friendly Name for this Exposure!"-name:...# declare properties of additional exposures
```

## Example[​](https://docs.getdbt.com/reference/exposure-properties?version=1.12#example "Direct link to Example")
models/jaffle/exposures.yml
```
exposures:-name: weekly_jaffle_metricslabel: Jaffles by the Week              # optionaltype: dashboard                         # requiredmaturity:# optionalurl: https://bi.tool/dashboards/1       # optionaldescription:# optional      Did someone say "exponential growth"?depends_on:# expected- ref('fct_orders')- ref('dim_customers')- source('gsheets', 'goals')- metric('count_orders')owner:name: Callum McDataemail: data@jaffleshop.com-name: jaffle_recommendermaturity: mediumtype: mlurl: https://jupyter.org/mycoolalgdescription:      Deep learning to power personalized "Discover Sandwiches Weekly"depends_on:- ref('fct_orders')owner:name: Data Science Drewemail: data@jaffleshop.com-name: jaffle_wrappedtype: applicationdescription: Tell users about their favorite jaffles of the yeardepends_on:[ ref('fct_orders') ]owner:{email: summer-intern@jaffleshop.com }
```

#### Project-level configs[​](https://docs.getdbt.com/reference/exposure-properties?version=1.12#project-level-configs "Direct link to Project-level configs")
You can define project-level configs for exposures in the `dbt_project.yml` file under the `exposures:` key using the `+` prefix. Currently, only the [`enabled` config](https://docs.getdbt.com/reference/resource-configs/enabled) is supported:
dbt_project.yml
```
name:'project_name'# rest of dbt_project.ymlexposures:+enabled:true
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
  * [Was this page helpful?](https://docs.getdbt.com/reference/exposure-properties?version=1.12#feedback-header)


## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices


--- SOURCE: https://docs.getdbt.com/reference/macro-properties ---

[Skip to main content](https://docs.getdbt.com/reference/macro-properties#__docusaurus_skipToContent_fallback)
[Join our free, Fast track to dbt workshop on April 7 or 8. Build and run your first dbt models!](https://www.getdbt.com/resources/webinars/fast-track-to-dbt-workshop/?utm_medium=internal&utm_source=docs&utm_campaign=q1-2027_fast-track-dbt-workshop_aw&utm_content=____&utm_term=all_all__)
Copy page
Copy page as Markdown for LLMs
[ Open in ChatGPT Ask questions about this page ](https://chatgpt.com/?hints=search&prompt=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fmacro-properties+so+I+can+ask+questions+about+it.)[ Open in Claude Ask questions about this page ](https://claude.ai/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fmacro-properties+so+I+can+ask+questions+about+it.)[ Open in Perplexity Ask questions about this page ](https://www.perplexity.ai/search/new?q=Read+from+https%3A%2F%2Fdocs.getdbt.com%2Freference%2Fmacro-properties+so+I+can+ask+questions+about+it.)
Macro properties can be declared in any `properties.yml` file. Macro properties are "special properties" in that you can't configure them in the `dbt_project.yml` file or using `config()` blocks. Refer to [ Configs and properties](https://docs.getdbt.com/reference/define-properties#which-properties-are-not-also-configs) for more info.
You can name these files `whatever_you_want.yml` and nest them arbitrarily deep in sub-folders.
macros/<filename>.yml
```
macros:-name: <macro name: <markdown_string>config:show: true | false: {<dictionary>}:-name: <arg name: <string>: <markdown_string>-...# declare properties of additional arguments-name:...# declare properties of additional macros
```

## Was this page helpful?
[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)
This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
0
## Privacy Preference Center
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. Click on the different category headings to find out more and change our default settings. However, blocking some types of cookies may impact your experience of the site and the services we are able to offer. [More information](https://www.getdbt.com/cloud/privacy-policy/)
Allow All
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
Strictly necessary cookies are necessary for the site to function properly and cannot be switched off in our systems. These cookies are usually only set in response to actions made by you that amount to a request for services, such as setting your privacy preferences, logging in, or filling in forms. You can set your browser to block or alert you about these cookies, but blocking these cookies will prevent the site from functioning properly. These cookies typically do not store personal data.
#### Performance Cookies
Always Active
Performance cookies allow us to count visits and traffic sources so we can measure and improve the performance of our sites. These cookies help us understand how our sites are being used, such as which sites are the most and least popular and how people navigate around the sites. The information collected in these cookies are aggregated, meaning that the do not relate to you personally. Opting out of these cookies will prevent us from knowing when you have visited our site and will prevent us from monitoring site performance. In some cases, these cookies may be sent to our third party service providers to help us manage these analytics.
#### Targeting Cookies
Always Active
Targeting cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant advertisements on other sites. These cookies do not store directly personal information, but are based on uniquely identifying your browser and device. If you do not allow these cookies, you will experience less targeted advertising.
#### Functional Cookies
Always Active
Functional cookies enable our sites to provide enhanced functionality and personalization. They may be set by us or by third party service providers whose services we have added to our sites. If you reject these cookies, then some or all of these services may not function properly.
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
checkbox label label
Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Confirm My Choices
