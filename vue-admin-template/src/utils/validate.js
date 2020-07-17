/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * @param {string} path
 * @returns {Boolean}
 */
export function isExternal(path) {
  return /^(https?:|mailto:|tel:)/.test(path)
}

/**
 * 判断输入的用户名是否合法
 * @param {string} str
 * @returns {Boolean}
 */
export function validUsername(str) {
  // 暂时设置为没有输入才报错
  if (!str) {
    return false
  } else {
    return true
  }
}
