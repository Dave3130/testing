# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11ll1lll_opy_, bstack11l1l111111_opy_, bstack11l11lll111_opy_
import tempfile
import json
bstack11111l1l111_opy_ = os.getenv(bstack11l11l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡈࡡࡉࡍࡑࡋࠢẻ"), None) or os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠤẼ"))
bstack11111ll1111_opy_ = os.path.join(bstack11l11l1_opy_ (u"ࠣ࡮ࡲ࡫ࠧẽ"), bstack11l11l1_opy_ (u"ࠩࡶࡨࡰ࠳ࡣ࡭࡫࠰ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬࠭Ế"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l11l1_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ế"),
      datefmt=bstack11l11l1_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩỀ"),
      stream=sys.stdout
    )
  return logger
def bstack1l11lll11ll_opy_():
  bstack11111l11l1l_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡉࡋࡂࡖࡉࠥề"), bstack11l11l1_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧỂ"))
  return logging.DEBUG if bstack11111l11l1l_opy_.lower() == bstack11l11l1_opy_ (u"ࠢࡵࡴࡸࡩࠧể") else logging.INFO
def bstack1ll11ll1l11_opy_():
  global bstack11111l1l111_opy_
  if os.path.exists(bstack11111l1l111_opy_):
    os.remove(bstack11111l1l111_opy_)
  if os.path.exists(bstack11111ll1111_opy_):
    os.remove(bstack11111ll1111_opy_)
def bstack111111l1l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111lll11l_opy_ = log_level
  if bstack11l11l1_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪỄ") in config and config[bstack11l11l1_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫễ")] in bstack11l1l111111_opy_:
    bstack11111lll11l_opy_ = bstack11l1l111111_opy_[config[bstack11l11l1_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬỆ")]]
  if config.get(bstack11l11l1_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ệ"), False):
    logging.getLogger().setLevel(bstack11111lll11l_opy_)
    return bstack11111lll11l_opy_
  global bstack11111l1l111_opy_
  bstack111111l1l_opy_()
  bstack11111ll1ll1_opy_ = logging.Formatter(
    fmt=bstack11l11l1_opy_ (u"ࠬࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨỈ"),
    datefmt=bstack11l11l1_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࡝ࠫỉ"),
  )
  bstack11111lll111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l1l111_opy_)
  file_handler.setFormatter(bstack11111ll1ll1_opy_)
  bstack11111lll111_opy_.setFormatter(bstack11111ll1ll1_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111lll111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l11l1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࡸࡥ࡮ࡱࡷࡩ࠳ࡸࡥ࡮ࡱࡷࡩࡤࡩ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࠩỊ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111lll111_opy_.setLevel(bstack11111lll11l_opy_)
  logging.getLogger().addHandler(bstack11111lll111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111lll11l_opy_
def bstack11111ll1lll_opy_(config):
  try:
    bstack11111l1llll_opy_ = set(bstack11l11lll111_opy_)
    bstack11111ll111l_opy_ = bstack11l11l1_opy_ (u"ࠨࠩị")
    with open(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬỌ")) as bstack11111l11ll1_opy_:
      bstack11111l1l11l_opy_ = bstack11111l11ll1_opy_.read()
      bstack11111ll111l_opy_ = re.sub(bstack11l11l1_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃࠨ࠴ࠪࠥ࡞ࡱࠫọ"), bstack11l11l1_opy_ (u"ࠫࠬỎ"), bstack11111l1l11l_opy_, flags=re.M)
      bstack11111ll111l_opy_ = re.sub(
        bstack11l11l1_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠨࠨỏ") + bstack11l11l1_opy_ (u"࠭ࡼࠨỐ").join(bstack11111l1llll_opy_) + bstack11l11l1_opy_ (u"ࠧࠪ࠰࠭ࠨࠬố"),
        bstack11l11l1_opy_ (u"ࡳࠩ࡟࠶࠿࡛ࠦࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪỒ"),
        bstack11111ll111l_opy_, flags=re.M | re.I
      )
    def bstack11111lll1l1_opy_(dic):
      bstack11111l1ll11_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1llll_opy_:
          bstack11111l1ll11_opy_[key] = bstack11l11l1_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ồ")
        else:
          if isinstance(value, dict):
            bstack11111l1ll11_opy_[key] = bstack11111lll1l1_opy_(value)
          else:
            bstack11111l1ll11_opy_[key] = value
      return bstack11111l1ll11_opy_
    bstack11111l1ll11_opy_ = bstack11111lll1l1_opy_(config)
    return {
      bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭Ổ"): bstack11111ll111l_opy_,
      bstack11l11l1_opy_ (u"ࠫ࡫࡯࡮ࡢ࡮ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧổ"): json.dumps(bstack11111l1ll11_opy_)
    }
  except Exception as e:
    return {}
def bstack11111ll11l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l11l1_opy_ (u"ࠬࡲ࡯ࡨࠩỖ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1l1ll_opy_ = os.path.join(log_dir, bstack11l11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹࠧỗ"))
  if not os.path.exists(bstack11111l1l1ll_opy_):
    bstack11111l11l11_opy_ = {
      bstack11l11l1_opy_ (u"ࠢࡪࡰ࡬ࡴࡦࡺࡨࠣỘ"): str(inipath),
      bstack11l11l1_opy_ (u"ࠣࡴࡲࡳࡹࡶࡡࡵࡪࠥộ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨỚ")), bstack11l11l1_opy_ (u"ࠪࡻࠬớ")) as bstack11111l1lll1_opy_:
      bstack11111l1lll1_opy_.write(json.dumps(bstack11111l11l11_opy_))
def bstack11111ll11ll_opy_():
  try:
    bstack11111l1l1ll_opy_ = os.path.join(os.getcwd(), bstack11l11l1_opy_ (u"ࠫࡱࡵࡧࠨỜ"), bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫờ"))
    if os.path.exists(bstack11111l1l1ll_opy_):
      with open(bstack11111l1l1ll_opy_, bstack11l11l1_opy_ (u"࠭ࡲࠨỞ")) as bstack11111l1lll1_opy_:
        bstack11111ll1l1l_opy_ = json.load(bstack11111l1lll1_opy_)
      return bstack11111ll1l1l_opy_.get(bstack11l11l1_opy_ (u"ࠧࡪࡰ࡬ࡴࡦࡺࡨࠨở"), bstack11l11l1_opy_ (u"ࠨࠩỠ")), bstack11111ll1l1l_opy_.get(bstack11l11l1_opy_ (u"ࠩࡵࡳࡴࡺࡰࡢࡶ࡫ࠫỡ"), bstack11l11l1_opy_ (u"ࠪࠫỢ"))
  except:
    pass
  return None, None
def bstack11111l111ll_opy_():
  try:
    bstack11111l1l1ll_opy_ = os.path.join(os.getcwd(), bstack11l11l1_opy_ (u"ࠫࡱࡵࡧࠨợ"), bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫỤ"))
    if os.path.exists(bstack11111l1l1ll_opy_):
      os.remove(bstack11111l1l1ll_opy_)
  except:
    pass
def bstack1l11l11l_opy_(config):
  try:
    from bstack_utils.helper import bstack11111111_opy_, bstack11l1lll1l_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l1l111_opy_
    if config.get(bstack11l11l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨụ"), False):
      return
    uuid = os.getenv(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬỦ")) if os.getenv(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ủ")) else bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦỨ"))
    if not uuid or uuid == bstack11l11l1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨứ"):
      return
    bstack11111ll1l11_opy_ = [bstack11l11l1_opy_ (u"ࠫࡷ࡫ࡱࡶ࡫ࡵࡩࡲ࡫࡮ࡵࡵ࠱ࡸࡽࡺࠧỪ"), bstack11l11l1_opy_ (u"ࠬࡖࡩࡱࡨ࡬ࡰࡪ࠭ừ"), bstack11l11l1_opy_ (u"࠭ࡰࡺࡲࡵࡳ࡯࡫ࡣࡵ࠰ࡷࡳࡲࡲࠧỬ"), bstack11111l1l111_opy_, bstack11111ll1111_opy_]
    bstack11111l1l1l1_opy_, root_path = bstack11111ll11ll_opy_()
    if bstack11111l1l1l1_opy_ != None:
      bstack11111ll1l11_opy_.append(bstack11111l1l1l1_opy_)
    if root_path != None:
      bstack11111ll1l11_opy_.append(os.path.join(root_path, bstack11l11l1_opy_ (u"ࠧࡤࡱࡱࡪࡹ࡫ࡳࡵ࠰ࡳࡽࠬử")))
    bstack111111l1l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧỮ") + uuid + bstack11l11l1_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪữ"))
    with tarfile.open(output_file, bstack11l11l1_opy_ (u"ࠥࡻ࠿࡭ࡺࠣỰ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111ll1l11_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111ll1lll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l11lll_opy_ = data.encode()
        tarinfo.size = len(bstack11111l11lll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l11lll_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l11l1_opy_ (u"ࠫࡩࡧࡴࡢࠩự"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l11l1_opy_ (u"ࠬࡸࡢࠨỲ")), bstack11l11l1_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫỳ")),
        bstack11l11l1_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩỴ"): uuid
      }
    )
    bstack11111l1ll1l_opy_ = bstack11l1lll1l_opy_(cli.config, [bstack11l11l1_opy_ (u"ࠣࡣࡳ࡭ࡸࠨỵ"), bstack11l11l1_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤỶ"), bstack11l11l1_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࠥỷ")], bstack11l11ll1lll_opy_)
    response = requests.post(
      bstack11l11l1_opy_ (u"ࠦࢀࢃ࠯ࡤ࡮࡬ࡩࡳࡺ࠭࡭ࡱࡪࡷ࠴ࡻࡰ࡭ࡱࡤࡨࠧỸ").format(bstack11111l1ll1l_opy_),
      data=multipart_data,
      headers={bstack11l11l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫỹ"): multipart_data.content_type},
      auth=(config[bstack11l11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨỺ")], config[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪỻ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧỼ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l11l1_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨỽ") + str(e))
  finally:
    try:
      bstack1ll11ll1l11_opy_()
      bstack11111l111ll_opy_()
    except:
      pass