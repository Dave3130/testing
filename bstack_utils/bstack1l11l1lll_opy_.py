# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11l1lll1_opy_, bstack11l11ll1l1l_opy_, bstack11l1l1l11l1_opy_
import tempfile
import json
bstack11111l1l1l1_opy_ = os.getenv(bstack111l1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡈࡡࡉࡍࡑࡋࠢỂ"), None) or os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠤể"))
bstack11111ll1ll1_opy_ = os.path.join(bstack111l1l_opy_ (u"ࠣ࡮ࡲ࡫ࠧỄ"), bstack111l1l_opy_ (u"ࠩࡶࡨࡰ࠳ࡣ࡭࡫࠰ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬࠭ễ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack111l1l_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭Ệ"),
      datefmt=bstack111l1l_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩệ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1ll1l11_opy_():
  bstack11111l111ll_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡉࡋࡂࡖࡉࠥỈ"), bstack111l1l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧỉ"))
  return logging.DEBUG if bstack11111l111ll_opy_.lower() == bstack111l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧỊ") else logging.INFO
def bstack1ll111lllll_opy_():
  global bstack11111l1l1l1_opy_
  if os.path.exists(bstack11111l1l1l1_opy_):
    os.remove(bstack11111l1l1l1_opy_)
  if os.path.exists(bstack11111ll1ll1_opy_):
    os.remove(bstack11111ll1ll1_opy_)
def bstack111l1ll1l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l11l1l_opy_ = log_level
  if bstack111l1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪị") in config and config[bstack111l1l_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫỌ")] in bstack11l11ll1l1l_opy_:
    bstack11111l11l1l_opy_ = bstack11l11ll1l1l_opy_[config[bstack111l1l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬọ")]]
  if config.get(bstack111l1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭Ỏ"), False):
    logging.getLogger().setLevel(bstack11111l11l1l_opy_)
    return bstack11111l11l1l_opy_
  global bstack11111l1l1l1_opy_
  bstack111l1ll1l_opy_()
  bstack11111ll1l11_opy_ = logging.Formatter(
    fmt=bstack111l1l_opy_ (u"ࠬࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨỏ"),
    datefmt=bstack111l1l_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࡝ࠫỐ"),
  )
  bstack111111lllll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l1l1l1_opy_)
  file_handler.setFormatter(bstack11111ll1l11_opy_)
  bstack111111lllll_opy_.setFormatter(bstack11111ll1l11_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111111lllll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack111l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࡸࡥ࡮ࡱࡷࡩ࠳ࡸࡥ࡮ࡱࡷࡩࡤࡩ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࠩố"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111111lllll_opy_.setLevel(bstack11111l11l1l_opy_)
  logging.getLogger().addHandler(bstack111111lllll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l11l1l_opy_
def bstack11111l1l11l_opy_(config):
  try:
    bstack11111l1l1ll_opy_ = set(bstack11l1l1l11l1_opy_)
    bstack11111ll1111_opy_ = bstack111l1l_opy_ (u"ࠨࠩỒ")
    with open(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬồ")) as bstack11111l11ll1_opy_:
      bstack11111ll11l1_opy_ = bstack11111l11ll1_opy_.read()
      bstack11111ll1111_opy_ = re.sub(bstack111l1l_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃࠨ࠴ࠪࠥ࡞ࡱࠫỔ"), bstack111l1l_opy_ (u"ࠫࠬổ"), bstack11111ll11l1_opy_, flags=re.M)
      bstack11111ll1111_opy_ = re.sub(
        bstack111l1l_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠨࠨỖ") + bstack111l1l_opy_ (u"࠭ࡼࠨỗ").join(bstack11111l1l1ll_opy_) + bstack111l1l_opy_ (u"ࠧࠪ࠰࠭ࠨࠬỘ"),
        bstack111l1l_opy_ (u"ࡳࠩ࡟࠶࠿࡛ࠦࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪộ"),
        bstack11111ll1111_opy_, flags=re.M | re.I
      )
    def bstack11111l1l111_opy_(dic):
      bstack11111l11l11_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1l1ll_opy_:
          bstack11111l11l11_opy_[key] = bstack111l1l_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭Ớ")
        else:
          if isinstance(value, dict):
            bstack11111l11l11_opy_[key] = bstack11111l1l111_opy_(value)
          else:
            bstack11111l11l11_opy_[key] = value
      return bstack11111l11l11_opy_
    bstack11111l11l11_opy_ = bstack11111l1l111_opy_(config)
    return {
      bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ớ"): bstack11111ll1111_opy_,
      bstack111l1l_opy_ (u"ࠫ࡫࡯࡮ࡢ࡮ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧỜ"): json.dumps(bstack11111l11l11_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l111l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠬࡲ࡯ࡨࠩờ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll111l_opy_ = os.path.join(log_dir, bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹࠧỞ"))
  if not os.path.exists(bstack11111ll111l_opy_):
    bstack11111l1lll1_opy_ = {
      bstack111l1l_opy_ (u"ࠢࡪࡰ࡬ࡴࡦࡺࡨࠣở"): str(inipath),
      bstack111l1l_opy_ (u"ࠣࡴࡲࡳࡹࡶࡡࡵࡪࠥỠ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨỡ")), bstack111l1l_opy_ (u"ࠪࡻࠬỢ")) as bstack11111l11lll_opy_:
      bstack11111l11lll_opy_.write(json.dumps(bstack11111l1lll1_opy_))
def bstack11111l1ll11_opy_():
  try:
    bstack11111ll111l_opy_ = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠫࡱࡵࡧࠨợ"), bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫỤ"))
    if os.path.exists(bstack11111ll111l_opy_):
      with open(bstack11111ll111l_opy_, bstack111l1l_opy_ (u"࠭ࡲࠨụ")) as bstack11111l11lll_opy_:
        bstack11111ll11ll_opy_ = json.load(bstack11111l11lll_opy_)
      return bstack11111ll11ll_opy_.get(bstack111l1l_opy_ (u"ࠧࡪࡰ࡬ࡴࡦࡺࡨࠨỦ"), bstack111l1l_opy_ (u"ࠨࠩủ")), bstack11111ll11ll_opy_.get(bstack111l1l_opy_ (u"ࠩࡵࡳࡴࡺࡰࡢࡶ࡫ࠫỨ"), bstack111l1l_opy_ (u"ࠪࠫứ"))
  except:
    pass
  return None, None
def bstack11111l1llll_opy_():
  try:
    bstack11111ll111l_opy_ = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠫࡱࡵࡧࠨỪ"), bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫừ"))
    if os.path.exists(bstack11111ll111l_opy_):
      os.remove(bstack11111ll111l_opy_)
  except:
    pass
def bstack1ll1111l_opy_(config):
  try:
    from bstack_utils.helper import bstack1lllll1l1_opy_, bstack1l1ll1ll1l_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l1l1l1_opy_
    if config.get(bstack111l1l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨỬ"), False):
      return
    uuid = os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬử")) if os.getenv(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭Ữ")) else bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦữ"))
    if not uuid or uuid == bstack111l1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨỰ"):
      return
    bstack11111l1111l_opy_ = [bstack111l1l_opy_ (u"ࠫࡷ࡫ࡱࡶ࡫ࡵࡩࡲ࡫࡮ࡵࡵ࠱ࡸࡽࡺࠧự"), bstack111l1l_opy_ (u"ࠬࡖࡩࡱࡨ࡬ࡰࡪ࠭Ỳ"), bstack111l1l_opy_ (u"࠭ࡰࡺࡲࡵࡳ࡯࡫ࡣࡵ࠰ࡷࡳࡲࡲࠧỳ"), bstack11111l1l1l1_opy_, bstack11111ll1ll1_opy_]
    bstack11111l1ll1l_opy_, root_path = bstack11111l1ll11_opy_()
    if bstack11111l1ll1l_opy_ != None:
      bstack11111l1111l_opy_.append(bstack11111l1ll1l_opy_)
    if root_path != None:
      bstack11111l1111l_opy_.append(os.path.join(root_path, bstack111l1l_opy_ (u"ࠧࡤࡱࡱࡪࡹ࡫ࡳࡵ࠰ࡳࡽࠬỴ")))
    bstack111l1ll1l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧỵ") + uuid + bstack111l1l_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪỶ"))
    with tarfile.open(output_file, bstack111l1l_opy_ (u"ࠥࡻ࠿࡭ࡺࠣỷ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1111l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1l11l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l11111_opy_ = data.encode()
        tarinfo.size = len(bstack11111l11111_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l11111_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack111l1l_opy_ (u"ࠫࡩࡧࡴࡢࠩỸ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack111l1l_opy_ (u"ࠬࡸࡢࠨỹ")), bstack111l1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫỺ")),
        bstack111l1l_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩỻ"): uuid
      }
    )
    bstack11111ll1l1l_opy_ = bstack1l1ll1ll1l_opy_(cli.config, [bstack111l1l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨỼ"), bstack111l1l_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤỽ"), bstack111l1l_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࠥỾ")], bstack11l11l1lll1_opy_)
    response = requests.post(
      bstack111l1l_opy_ (u"ࠦࢀࢃ࠯ࡤ࡮࡬ࡩࡳࡺ࠭࡭ࡱࡪࡷ࠴ࡻࡰ࡭ࡱࡤࡨࠧỿ").format(bstack11111ll1l1l_opy_),
      data=multipart_data,
      headers={bstack111l1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫἀ"): multipart_data.content_type},
      auth=(config[bstack111l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨἁ")], config[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪἂ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧἃ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack111l1l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨἄ") + str(e))
  finally:
    try:
      bstack1ll111lllll_opy_()
      bstack11111l1llll_opy_()
    except:
      pass