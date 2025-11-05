# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l111ll1_opy_, bstack11l1l11111l_opy_, bstack11l11l11l1l_opy_
import tempfile
import json
bstack11111l111l1_opy_ = os.getenv(bstack1lll11l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡈࡡࡉࡍࡑࡋࠢỞ"), None) or os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠤở"))
bstack11111l11ll1_opy_ = os.path.join(bstack1lll11l_opy_ (u"ࠣ࡮ࡲ࡫ࠧỠ"), bstack1lll11l_opy_ (u"ࠩࡶࡨࡰ࠳ࡣ࡭࡫࠰ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬࠭ỡ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1lll11l_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭Ợ"),
      datefmt=bstack1lll11l_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩợ"),
      stream=sys.stdout
    )
  return logger
def bstack1l11ll111l1_opy_():
  bstack11111ll1111_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇࡏࡎࡂࡔ࡜ࡣࡉࡋࡂࡖࡉࠥỤ"), bstack1lll11l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧụ"))
  return logging.DEBUG if bstack11111ll1111_opy_.lower() == bstack1lll11l_opy_ (u"ࠢࡵࡴࡸࡩࠧỦ") else logging.INFO
def bstack1ll11l11l11_opy_():
  global bstack11111l111l1_opy_
  if os.path.exists(bstack11111l111l1_opy_):
    os.remove(bstack11111l111l1_opy_)
  if os.path.exists(bstack11111l11ll1_opy_):
    os.remove(bstack11111l11ll1_opy_)
def bstack1ll11ll111_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1l1ll_opy_ = log_level
  if bstack1lll11l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪủ") in config and config[bstack1lll11l_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫỨ")] in bstack11l1l11111l_opy_:
    bstack11111l1l1ll_opy_ = bstack11l1l11111l_opy_[config[bstack1lll11l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬứ")]]
  if config.get(bstack1lll11l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭Ừ"), False):
    logging.getLogger().setLevel(bstack11111l1l1ll_opy_)
    return bstack11111l1l1ll_opy_
  global bstack11111l111l1_opy_
  bstack1ll11ll111_opy_()
  bstack11111l11l11_opy_ = logging.Formatter(
    fmt=bstack1lll11l_opy_ (u"ࠬࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨừ"),
    datefmt=bstack1lll11l_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࡝ࠫỬ"),
  )
  bstack111111lll1l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l111l1_opy_)
  file_handler.setFormatter(bstack11111l11l11_opy_)
  bstack111111lll1l_opy_.setFormatter(bstack11111l11l11_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111111lll1l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1lll11l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࡸࡥ࡮ࡱࡷࡩ࠳ࡸࡥ࡮ࡱࡷࡩࡤࡩ࡯࡯ࡰࡨࡧࡹ࡯࡯࡯ࠩử"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111111lll1l_opy_.setLevel(bstack11111l1l1ll_opy_)
  logging.getLogger().addHandler(bstack111111lll1l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1l1ll_opy_
def bstack11111l1lll1_opy_(config):
  try:
    bstack11111l1llll_opy_ = set(bstack11l11l11l1l_opy_)
    bstack11111ll111l_opy_ = bstack1lll11l_opy_ (u"ࠨࠩỮ")
    with open(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬữ")) as bstack11111ll11l1_opy_:
      bstack11111l1ll11_opy_ = bstack11111ll11l1_opy_.read()
      bstack11111ll111l_opy_ = re.sub(bstack1lll11l_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃࠨ࠴ࠪࠥ࡞ࡱࠫỰ"), bstack1lll11l_opy_ (u"ࠫࠬự"), bstack11111l1ll11_opy_, flags=re.M)
      bstack11111ll111l_opy_ = re.sub(
        bstack1lll11l_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠨࠨỲ") + bstack1lll11l_opy_ (u"࠭ࡼࠨỳ").join(bstack11111l1llll_opy_) + bstack1lll11l_opy_ (u"ࠧࠪ࠰࠭ࠨࠬỴ"),
        bstack1lll11l_opy_ (u"ࡳࠩ࡟࠶࠿࡛ࠦࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪỵ"),
        bstack11111ll111l_opy_, flags=re.M | re.I
      )
    def bstack11111l11111_opy_(dic):
      bstack111111lll11_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1llll_opy_:
          bstack111111lll11_opy_[key] = bstack1lll11l_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭Ỷ")
        else:
          if isinstance(value, dict):
            bstack111111lll11_opy_[key] = bstack11111l11111_opy_(value)
          else:
            bstack111111lll11_opy_[key] = value
      return bstack111111lll11_opy_
    bstack111111lll11_opy_ = bstack11111l11111_opy_(config)
    return {
      bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ỷ"): bstack11111ll111l_opy_,
      bstack1lll11l_opy_ (u"ࠫ࡫࡯࡮ࡢ࡮ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧỸ"): json.dumps(bstack111111lll11_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l11lll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡨࠩỹ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1l111_opy_ = os.path.join(log_dir, bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹࠧỺ"))
  if not os.path.exists(bstack11111l1l111_opy_):
    bstack11111l11l1l_opy_ = {
      bstack1lll11l_opy_ (u"ࠢࡪࡰ࡬ࡴࡦࡺࡨࠣỻ"): str(inipath),
      bstack1lll11l_opy_ (u"ࠣࡴࡲࡳࡹࡶࡡࡵࡪࠥỼ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1lll11l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨỽ")), bstack1lll11l_opy_ (u"ࠪࡻࠬỾ")) as bstack111111llll1_opy_:
      bstack111111llll1_opy_.write(json.dumps(bstack11111l11l1l_opy_))
def bstack11111l1l1l1_opy_():
  try:
    bstack11111l1l111_opy_ = os.path.join(os.getcwd(), bstack1lll11l_opy_ (u"ࠫࡱࡵࡧࠨỿ"), bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫἀ"))
    if os.path.exists(bstack11111l1l111_opy_):
      with open(bstack11111l1l111_opy_, bstack1lll11l_opy_ (u"࠭ࡲࠨἁ")) as bstack111111llll1_opy_:
        bstack11111l111ll_opy_ = json.load(bstack111111llll1_opy_)
      return bstack11111l111ll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡪࡰ࡬ࡴࡦࡺࡨࠨἂ"), bstack1lll11l_opy_ (u"ࠨࠩἃ")), bstack11111l111ll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡵࡳࡴࡺࡰࡢࡶ࡫ࠫἄ"), bstack1lll11l_opy_ (u"ࠪࠫἅ"))
  except:
    pass
  return None, None
def bstack11111l1ll1l_opy_():
  try:
    bstack11111l1l111_opy_ = os.path.join(os.getcwd(), bstack1lll11l_opy_ (u"ࠫࡱࡵࡧࠨἆ"), bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫἇ"))
    if os.path.exists(bstack11111l1l111_opy_):
      os.remove(bstack11111l1l111_opy_)
  except:
    pass
def bstack1l11llll_opy_(config):
  try:
    from bstack_utils.helper import bstack111ll1l1_opy_, bstack11llll111_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l111l1_opy_
    if config.get(bstack1lll11l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨἈ"), False):
      return
    uuid = os.getenv(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬἉ")) if os.getenv(bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭Ἂ")) else bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦἋ"))
    if not uuid or uuid == bstack1lll11l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨἌ"):
      return
    bstack11111ll11ll_opy_ = [bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡱࡶ࡫ࡵࡩࡲ࡫࡮ࡵࡵ࠱ࡸࡽࡺࠧἍ"), bstack1lll11l_opy_ (u"ࠬࡖࡩࡱࡨ࡬ࡰࡪ࠭Ἆ"), bstack1lll11l_opy_ (u"࠭ࡰࡺࡲࡵࡳ࡯࡫ࡣࡵ࠰ࡷࡳࡲࡲࠧἏ"), bstack11111l111l1_opy_, bstack11111l11ll1_opy_]
    bstack11111l1l11l_opy_, root_path = bstack11111l1l1l1_opy_()
    if bstack11111l1l11l_opy_ != None:
      bstack11111ll11ll_opy_.append(bstack11111l1l11l_opy_)
    if root_path != None:
      bstack11111ll11ll_opy_.append(os.path.join(root_path, bstack1lll11l_opy_ (u"ࠧࡤࡱࡱࡪࡹ࡫ࡳࡵ࠰ࡳࡽࠬἐ")))
    bstack1ll11ll111_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠮࡮ࡲ࡫ࡸ࠳ࠧἑ") + uuid + bstack1lll11l_opy_ (u"ࠩ࠱ࡸࡦࡸ࠮ࡨࡼࠪἒ"))
    with tarfile.open(output_file, bstack1lll11l_opy_ (u"ࠥࡻ࠿࡭ࡺࠣἓ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111ll11ll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1lll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1111l_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1111l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1111l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1lll11l_opy_ (u"ࠫࡩࡧࡴࡢࠩἔ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1lll11l_opy_ (u"ࠬࡸࡢࠨἕ")), bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳ࡽ࠳ࡧࡻ࡫ࡳࠫ἖")),
        bstack1lll11l_opy_ (u"ࠧࡤ࡮࡬ࡩࡳࡺࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ἗"): uuid
      }
    )
    bstack111111lllll_opy_ = bstack11llll111_opy_(cli.config, [bstack1lll11l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨἘ"), bstack1lll11l_opy_ (u"ࠤࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠤἙ"), bstack1lll11l_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࠥἚ")], bstack11l1l111ll1_opy_)
    response = requests.post(
      bstack1lll11l_opy_ (u"ࠦࢀࢃ࠯ࡤ࡮࡬ࡩࡳࡺ࠭࡭ࡱࡪࡷ࠴ࡻࡰ࡭ࡱࡤࡨࠧἛ").format(bstack111111lllll_opy_),
      data=multipart_data,
      headers={bstack1lll11l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫἜ"): multipart_data.content_type},
      auth=(config[bstack1lll11l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨἝ")], config[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ἞")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1lll11l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲ࡯ࡳࡦࡪࠠ࡭ࡱࡪࡷ࠿ࠦࠧ἟") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1lll11l_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹ࠺ࠨἠ") + str(e))
  finally:
    try:
      bstack1ll11l11l11_opy_()
      bstack11111l1ll1l_opy_()
    except:
      pass