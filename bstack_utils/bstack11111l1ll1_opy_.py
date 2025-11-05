# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11lll1l1_opy_, bstack11l1l111ll1_opy_, bstack11l11ll111l_opy_
import tempfile
import json
bstack111111lll11_opy_ = os.getenv(bstack11ll1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡇࡠࡈࡌࡐࡊࠨỹ"), None) or os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡪࡥࡣࡷࡪ࠲ࡱࡵࡧࠣỺ"))
bstack11111l1l1ll_opy_ = os.path.join(bstack11ll1ll_opy_ (u"ࠢ࡭ࡱࡪࠦỻ"), bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯࠲ࡩ࡬ࡪ࠯ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠬỼ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11ll1ll_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬỽ"),
      datefmt=bstack11ll1ll_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨỾ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1ll111l_opy_():
  bstack11111l111l1_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆࡎࡔࡁࡓ࡛ࡢࡈࡊࡈࡕࡈࠤỿ"), bstack11ll1ll_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦἀ"))
  return logging.DEBUG if bstack11111l111l1_opy_.lower() == bstack11ll1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦἁ") else logging.INFO
def bstack1ll11lll1ll_opy_():
  global bstack111111lll11_opy_
  if os.path.exists(bstack111111lll11_opy_):
    os.remove(bstack111111lll11_opy_)
  if os.path.exists(bstack11111l1l1ll_opy_):
    os.remove(bstack11111l1l1ll_opy_)
def bstack1l1lll1ll1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1ll11_opy_ = log_level
  if bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩἂ") in config and config[bstack11ll1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪἃ")] in bstack11l1l111ll1_opy_:
    bstack11111l1ll11_opy_ = bstack11l1l111ll1_opy_[config[bstack11ll1ll_opy_ (u"ࠩ࡯ࡳ࡬ࡒࡥࡷࡧ࡯ࠫἄ")]]
  if config.get(bstack11ll1ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬἅ"), False):
    logging.getLogger().setLevel(bstack11111l1ll11_opy_)
    return bstack11111l1ll11_opy_
  global bstack111111lll11_opy_
  bstack1l1lll1ll1_opy_()
  bstack111111lll1l_opy_ = logging.Formatter(
    fmt=bstack11ll1ll_opy_ (u"ࠫࠪ࠮ࡡࡴࡥࡷ࡭ࡲ࡫ࠩࡴࠢ࡞ࠩ࠭ࡴࡡ࡮ࡧࠬࡷࡢࡡࠥࠩ࡮ࡨࡺࡪࡲ࡮ࡢ࡯ࡨ࠭ࡸࡣࠠ࠮ࠢࠨࠬࡲ࡫ࡳࡴࡣࡪࡩ࠮ࡹࠧἆ"),
    datefmt=bstack11ll1ll_opy_ (u"࡙ࠬࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࡜ࠪἇ"),
  )
  bstack11111l11l1l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack111111lll11_opy_)
  file_handler.setFormatter(bstack111111lll1l_opy_)
  bstack11111l11l1l_opy_.setFormatter(bstack111111lll1l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l11l1l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11ll1ll_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࡷ࡫࡭ࡰࡶࡨ࠲ࡷ࡫࡭ࡰࡶࡨࡣࡨࡵ࡮࡯ࡧࡦࡸ࡮ࡵ࡮ࠨἈ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l11l1l_opy_.setLevel(bstack11111l1ll11_opy_)
  logging.getLogger().addHandler(bstack11111l11l1l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1ll11_opy_
def bstack111111ll11l_opy_(config):
  try:
    bstack111111lllll_opy_ = set(bstack11l11ll111l_opy_)
    bstack11111l1ll1l_opy_ = bstack11ll1ll_opy_ (u"ࠧࠨἉ")
    with open(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫἊ")) as bstack11111l1l11l_opy_:
      bstack11111l1111l_opy_ = bstack11111l1l11l_opy_.read()
      bstack11111l1ll1l_opy_ = re.sub(bstack11ll1ll_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠧ࠳࠰ࠤ࡝ࡰࠪἋ"), bstack11ll1ll_opy_ (u"ࠪࠫἌ"), bstack11111l1111l_opy_, flags=re.M)
      bstack11111l1ll1l_opy_ = re.sub(
        bstack11ll1ll_opy_ (u"ࡶࠬࡤࠨ࡝ࡵ࠮࠭ࡄ࠮ࠧἍ") + bstack11ll1ll_opy_ (u"ࠬࢂࠧἎ").join(bstack111111lllll_opy_) + bstack11ll1ll_opy_ (u"࠭ࠩ࠯ࠬࠧࠫἏ"),
        bstack11ll1ll_opy_ (u"ࡲࠨ࡞࠵࠾ࠥࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩἐ"),
        bstack11111l1ll1l_opy_, flags=re.M | re.I
      )
    def bstack111111llll1_opy_(dic):
      bstack111111ll1ll_opy_ = {}
      for key, value in dic.items():
        if key in bstack111111lllll_opy_:
          bstack111111ll1ll_opy_[key] = bstack11ll1ll_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬἑ")
        else:
          if isinstance(value, dict):
            bstack111111ll1ll_opy_[key] = bstack111111llll1_opy_(value)
          else:
            bstack111111ll1ll_opy_[key] = value
      return bstack111111ll1ll_opy_
    bstack111111ll1ll_opy_ = bstack111111llll1_opy_(config)
    return {
      bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬἒ"): bstack11111l1ll1l_opy_,
      bstack11ll1ll_opy_ (u"ࠪࡪ࡮ࡴࡡ࡭ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ἓ"): json.dumps(bstack111111ll1ll_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l11ll1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11ll1ll_opy_ (u"ࠫࡱࡵࡧࠨἔ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1llll_opy_ = os.path.join(log_dir, bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠭ἕ"))
  if not os.path.exists(bstack11111l1llll_opy_):
    bstack11111l1l111_opy_ = {
      bstack11ll1ll_opy_ (u"ࠨࡩ࡯࡫ࡳࡥࡹ࡮ࠢ἖"): str(inipath),
      bstack11ll1ll_opy_ (u"ࠢࡳࡱࡲࡸࡵࡧࡴࡩࠤ἗"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11ll1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧἘ")), bstack11ll1ll_opy_ (u"ࠩࡺࠫἙ")) as bstack11111l11l11_opy_:
      bstack11111l11l11_opy_.write(json.dumps(bstack11111l1l111_opy_))
def bstack11111l11111_opy_():
  try:
    bstack11111l1llll_opy_ = os.path.join(os.getcwd(), bstack11ll1ll_opy_ (u"ࠪࡰࡴ࡭ࠧἚ"), bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪἛ"))
    if os.path.exists(bstack11111l1llll_opy_):
      with open(bstack11111l1llll_opy_, bstack11ll1ll_opy_ (u"ࠬࡸࠧἜ")) as bstack11111l11l11_opy_:
        bstack111111ll1l1_opy_ = json.load(bstack11111l11l11_opy_)
      return bstack111111ll1l1_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡩ࡯࡫ࡳࡥࡹ࡮ࠧἝ"), bstack11ll1ll_opy_ (u"ࠧࠨ἞")), bstack111111ll1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡴࡲࡳࡹࡶࡡࡵࡪࠪ἟"), bstack11ll1ll_opy_ (u"ࠩࠪἠ"))
  except:
    pass
  return None, None
def bstack111111ll111_opy_():
  try:
    bstack11111l1llll_opy_ = os.path.join(os.getcwd(), bstack11ll1ll_opy_ (u"ࠪࡰࡴ࡭ࠧἡ"), bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪἢ"))
    if os.path.exists(bstack11111l1llll_opy_):
      os.remove(bstack11111l1llll_opy_)
  except:
    pass
def bstack1l1111ll_opy_(config):
  try:
    from bstack_utils.helper import bstack1llllll1l_opy_, bstack111l111l11_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack111111lll11_opy_
    if config.get(bstack11ll1ll_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧἣ"), False):
      return
    uuid = os.getenv(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫἤ")) if os.getenv(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬἥ")) else bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥἦ"))
    if not uuid or uuid == bstack11ll1ll_opy_ (u"ࠩࡱࡹࡱࡲࠧἧ"):
      return
    bstack11111l111ll_opy_ = [bstack11ll1ll_opy_ (u"ࠪࡶࡪࡷࡵࡪࡴࡨࡱࡪࡴࡴࡴ࠰ࡷࡼࡹ࠭Ἠ"), bstack11ll1ll_opy_ (u"ࠫࡕ࡯ࡰࡧ࡫࡯ࡩࠬἩ"), bstack11ll1ll_opy_ (u"ࠬࡶࡹࡱࡴࡲ࡮ࡪࡩࡴ࠯ࡶࡲࡱࡱ࠭Ἢ"), bstack111111lll11_opy_, bstack11111l1l1ll_opy_]
    bstack11111l11lll_opy_, root_path = bstack11111l11111_opy_()
    if bstack11111l11lll_opy_ != None:
      bstack11111l111ll_opy_.append(bstack11111l11lll_opy_)
    if root_path != None:
      bstack11111l111ll_opy_.append(os.path.join(root_path, bstack11ll1ll_opy_ (u"࠭ࡣࡰࡰࡩࡸࡪࡹࡴ࠯ࡲࡼࠫἫ")))
    bstack1l1lll1ll1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠭࡭ࡱࡪࡷ࠲࠭Ἤ") + uuid + bstack11ll1ll_opy_ (u"ࠨ࠰ࡷࡥࡷ࠴ࡧࡻࠩἭ"))
    with tarfile.open(output_file, bstack11ll1ll_opy_ (u"ࠤࡺ࠾࡬ࢀࠢἮ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l111ll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111111ll11l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1l1l1_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1l1l1_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1l1l1_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11ll1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨἯ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11ll1ll_opy_ (u"ࠫࡷࡨࠧἰ")), bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲ࡼ࠲࡭ࡺࡪࡲࠪἱ")),
        bstack11ll1ll_opy_ (u"࠭ࡣ࡭࡫ࡨࡲࡹࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨἲ"): uuid
      }
    )
    bstack11111l1lll1_opy_ = bstack111l111l11_opy_(cli.config, [bstack11ll1ll_opy_ (u"ࠢࡢࡲ࡬ࡷࠧἳ"), bstack11ll1ll_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣἴ"), bstack11ll1ll_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࠤἵ")], bstack11l11lll1l1_opy_)
    response = requests.post(
      bstack11ll1ll_opy_ (u"ࠥࡿࢂ࠵ࡣ࡭࡫ࡨࡲࡹ࠳࡬ࡰࡩࡶ࠳ࡺࡶ࡬ࡰࡣࡧࠦἶ").format(bstack11111l1lll1_opy_),
      data=multipart_data,
      headers={bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪἷ"): multipart_data.content_type},
      auth=(config[bstack11ll1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧἸ")], config[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩἹ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11ll1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱ࡮ࡲࡥࡩࠦ࡬ࡰࡩࡶ࠾ࠥ࠭Ἲ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11ll1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡ࡮ࡲ࡫ࡸࡀࠧἻ") + str(e))
  finally:
    try:
      bstack1ll11lll1ll_opy_()
      bstack111111ll111_opy_()
    except:
      pass