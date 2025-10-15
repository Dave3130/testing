# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l1ll1l1_opy_, bstack11l1l11l11l_opy_, bstack11l1l111111_opy_
import tempfile
import json
bstack11111ll1l1l_opy_ = os.getenv(bstack1ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡈࡡࡉࡍࡑࡋࠢẟ"), None) or os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠤẠ"))
bstack1111l11111l_opy_ = os.path.join(bstack1ll1l_opy_ (u"ࠣ࡮ࡲ࡫ࠧạ"), bstack1ll1l_opy_ (u"ࠩࡶࡨࡰ࠳ࡣ࡭࡫࠰ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬࠭Ả"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1ll1l_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ả"),
      datefmt=bstack1ll1l_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩẤ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1llll11_opy_():
  bstack11111ll1111_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡉࡋࡂࡖࡉࠥấ"), bstack1ll1l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧẦ"))
  return logging.DEBUG if bstack11111ll1111_opy_.lower() == bstack1ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧầ") else logging.INFO
def bstack1ll11l1lll1_opy_():
  global bstack11111ll1l1l_opy_
  if os.path.exists(bstack11111ll1l1l_opy_):
    os.remove(bstack11111ll1l1l_opy_)
  if os.path.exists(bstack1111l11111l_opy_):
    os.remove(bstack1111l11111l_opy_)
def bstack1l1111111_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111lll111_opy_ = log_level
  if bstack1ll1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪẨ") in config and config[bstack1ll1l_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫẩ")] in bstack11l1l11l11l_opy_:
    bstack11111lll111_opy_ = bstack11l1l11l11l_opy_[config[bstack1ll1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬẪ")]]
  if config.get(bstack1ll1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ẫ"), False):
    logging.getLogger().setLevel(bstack11111lll111_opy_)
    return bstack11111lll111_opy_
  global bstack11111ll1l1l_opy_
  bstack1l1111111_opy_()
  bstack11111l1l1ll_opy_ = logging.Formatter(
    fmt=bstack1ll1l_opy_ (u"ࠬࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨẬ"),
    datefmt=bstack1ll1l_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࡝ࠫậ"),
  )
  bstack11111ll111l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111ll1l1l_opy_)
  file_handler.setFormatter(bstack11111l1l1ll_opy_)
  bstack11111ll111l_opy_.setFormatter(bstack11111l1l1ll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll111l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1ll1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࡸࡥ࡮ࡱࡷࡩ࠳ࡸࡥ࡮ࡱࡷࡩࡤࡩ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࠩẮ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll111l_opy_.setLevel(bstack11111lll111_opy_)
  logging.getLogger().addHandler(bstack11111ll111l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111lll111_opy_
def bstack11111lll11l_opy_(config):
  try:
    bstack11111lllll1_opy_ = set(bstack11l1l111111_opy_)
    bstack11111l1llll_opy_ = bstack1ll1l_opy_ (u"ࠨࠩắ")
    with open(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬẰ")) as bstack11111lll1l1_opy_:
      bstack11111ll11l1_opy_ = bstack11111lll1l1_opy_.read()
      bstack11111l1llll_opy_ = re.sub(bstack1ll1l_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃࠨ࠴ࠪࠥ࡞ࡱࠫằ"), bstack1ll1l_opy_ (u"ࠫࠬẲ"), bstack11111ll11l1_opy_, flags=re.M)
      bstack11111l1llll_opy_ = re.sub(
        bstack1ll1l_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠨࠨẳ") + bstack1ll1l_opy_ (u"࠭ࡼࠨẴ").join(bstack11111lllll1_opy_) + bstack1ll1l_opy_ (u"ࠧࠪ࠰࠭ࠨࠬẵ"),
        bstack1ll1l_opy_ (u"ࡳࠩ࡟࠶࠿࡛ࠦࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪẶ"),
        bstack11111l1llll_opy_, flags=re.M | re.I
      )
    def bstack11111ll1ll1_opy_(dic):
      bstack11111l1lll1_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111lllll1_opy_:
          bstack11111l1lll1_opy_[key] = bstack1ll1l_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ặ")
        else:
          if isinstance(value, dict):
            bstack11111l1lll1_opy_[key] = bstack11111ll1ll1_opy_(value)
          else:
            bstack11111l1lll1_opy_[key] = value
      return bstack11111l1lll1_opy_
    bstack11111l1lll1_opy_ = bstack11111ll1ll1_opy_(config)
    return {
      bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭Ẹ"): bstack11111l1llll_opy_,
      bstack1ll1l_opy_ (u"ࠫ࡫࡯࡮ࡢ࡮ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧẹ"): json.dumps(bstack11111l1lll1_opy_)
    }
  except Exception as e:
    return {}
def bstack11111ll1l11_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1ll1l_opy_ (u"ࠬࡲ࡯ࡨࠩẺ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll1lll_opy_ = os.path.join(log_dir, bstack1ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹࠧẻ"))
  if not os.path.exists(bstack11111ll1lll_opy_):
    bstack11111llllll_opy_ = {
      bstack1ll1l_opy_ (u"ࠢࡪࡰ࡬ࡴࡦࡺࡨࠣẼ"): str(inipath),
      bstack1ll1l_opy_ (u"ࠣࡴࡲࡳࡹࡶࡡࡵࡪࠥẽ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨẾ")), bstack1ll1l_opy_ (u"ࠪࡻࠬế")) as bstack11111llll1l_opy_:
      bstack11111llll1l_opy_.write(json.dumps(bstack11111llllll_opy_))
def bstack1111l1111l1_opy_():
  try:
    bstack11111ll1lll_opy_ = os.path.join(os.getcwd(), bstack1ll1l_opy_ (u"ࠫࡱࡵࡧࠨỀ"), bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫề"))
    if os.path.exists(bstack11111ll1lll_opy_):
      with open(bstack11111ll1lll_opy_, bstack1ll1l_opy_ (u"࠭ࡲࠨỂ")) as bstack11111llll1l_opy_:
        bstack11111l1ll11_opy_ = json.load(bstack11111llll1l_opy_)
      return bstack11111l1ll11_opy_.get(bstack1ll1l_opy_ (u"ࠧࡪࡰ࡬ࡴࡦࡺࡨࠨể"), bstack1ll1l_opy_ (u"ࠨࠩỄ")), bstack11111l1ll11_opy_.get(bstack1ll1l_opy_ (u"ࠩࡵࡳࡴࡺࡰࡢࡶ࡫ࠫễ"), bstack1ll1l_opy_ (u"ࠪࠫỆ"))
  except:
    pass
  return None, None
def bstack11111l1ll1l_opy_():
  try:
    bstack11111ll1lll_opy_ = os.path.join(os.getcwd(), bstack1ll1l_opy_ (u"ࠫࡱࡵࡧࠨệ"), bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫỈ"))
    if os.path.exists(bstack11111ll1lll_opy_):
      os.remove(bstack11111ll1lll_opy_)
  except:
    pass
def bstack1l1lll1l_opy_(config):
  try:
    from bstack_utils.helper import bstack111111ll_opy_, bstack1ll11l1l1_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111ll1l1l_opy_
    if config.get(bstack1ll1l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨỉ"), False):
      return
    uuid = os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬỊ")) if os.getenv(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ị")) else bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦỌ"))
    if not uuid or uuid == bstack1ll1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨọ"):
      return
    bstack11111ll11ll_opy_ = [bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡱࡶ࡫ࡵࡩࡲ࡫࡮ࡵࡵ࠱ࡸࡽࡺࠧỎ"), bstack1ll1l_opy_ (u"ࠬࡖࡩࡱࡨ࡬ࡰࡪ࠭ỏ"), bstack1ll1l_opy_ (u"࠭ࡰࡺࡲࡵࡳ࡯࡫ࡣࡵ࠰ࡷࡳࡲࡲࠧỐ"), bstack11111ll1l1l_opy_, bstack1111l11111l_opy_]
    bstack11111lll1ll_opy_, root_path = bstack1111l1111l1_opy_()
    if bstack11111lll1ll_opy_ != None:
      bstack11111ll11ll_opy_.append(bstack11111lll1ll_opy_)
    if root_path != None:
      bstack11111ll11ll_opy_.append(os.path.join(root_path, bstack1ll1l_opy_ (u"ࠧࡤࡱࡱࡪࡹ࡫ࡳࡵ࠰ࡳࡽࠬố")))
    bstack1l1111111_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧỒ") + uuid + bstack1ll1l_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪồ"))
    with tarfile.open(output_file, bstack1ll1l_opy_ (u"ࠥࡻ࠿࡭ࡺࠣỔ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111ll11ll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111lll11l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111llll11_opy_ = data.encode()
        tarinfo.size = len(bstack11111llll11_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111llll11_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1ll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩổ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1ll1l_opy_ (u"ࠬࡸࡢࠨỖ")), bstack1ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫỗ")),
        bstack1ll1l_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩỘ"): uuid
      }
    )
    bstack1111l111111_opy_ = bstack1ll11l1l1_opy_(cli.config, [bstack1ll1l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨộ"), bstack1ll1l_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤỚ"), bstack1ll1l_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࠥớ")], bstack11l1l1ll1l1_opy_)
    response = requests.post(
      bstack1ll1l_opy_ (u"ࠦࢀࢃ࠯ࡤ࡮࡬ࡩࡳࡺ࠭࡭ࡱࡪࡷ࠴ࡻࡰ࡭ࡱࡤࡨࠧỜ").format(bstack1111l111111_opy_),
      data=multipart_data,
      headers={bstack1ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫờ"): multipart_data.content_type},
      auth=(config[bstack1ll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨỞ")], config[bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪở")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧỠ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1ll1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨỡ") + str(e))
  finally:
    try:
      bstack1ll11l1lll1_opy_()
      bstack11111l1ll1l_opy_()
    except:
      pass