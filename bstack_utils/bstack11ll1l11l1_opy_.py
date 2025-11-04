# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11ll1lll_opy_, bstack11l11lll1l1_opy_, bstack11l11l1lll1_opy_
import tempfile
import json
bstack11111l1l111_opy_ = os.getenv(bstack11l1111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡌࡥࡆࡊࡎࡈࠦỷ"), None) or os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬ࠨỸ"))
bstack11111l1l1ll_opy_ = os.path.join(bstack11l1111_opy_ (u"ࠧࡲ࡯ࡨࠤỹ"), bstack11l1111_opy_ (u"࠭ࡳࡥ࡭࠰ࡧࡱ࡯࠭ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪỺ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l1111_opy_ (u"ࠧࠦࠪࡤࡷࡨࡺࡩ࡮ࡧࠬࡷࠥࡡࠥࠩࡰࡤࡱࡪ࠯ࡳ࡞࡝ࠨࠬࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠩࡴ࡟ࠣ࠱ࠥࠫࠨ࡮ࡧࡶࡷࡦ࡭ࡥࠪࡵࠪỻ"),
      datefmt=bstack11l1111_opy_ (u"ࠨࠧ࡜࠱ࠪࡳ࠭ࠦࡦࡗࠩࡍࡀࠥࡎ࠼ࠨࡗ࡟࠭Ỽ"),
      stream=sys.stdout
    )
  return logger
def bstack1l11l1llll1_opy_():
  bstack111111llll1_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡆࡈࡆ࡚ࡍࠢỽ"), bstack11l1111_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤỾ"))
  return logging.DEBUG if bstack111111llll1_opy_.lower() == bstack11l1111_opy_ (u"ࠦࡹࡸࡵࡦࠤỿ") else logging.INFO
def bstack1ll11111ll1_opy_():
  global bstack11111l1l111_opy_
  if os.path.exists(bstack11111l1l111_opy_):
    os.remove(bstack11111l1l111_opy_)
  if os.path.exists(bstack11111l1l1ll_opy_):
    os.remove(bstack11111l1l1ll_opy_)
def bstack111lll11l_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack111111lll1l_opy_ = log_level
  if bstack11l1111_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧἀ") in config and config[bstack11l1111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨἁ")] in bstack11l11lll1l1_opy_:
    bstack111111lll1l_opy_ = bstack11l11lll1l1_opy_[config[bstack11l1111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩἂ")]]
  if config.get(bstack11l1111_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪἃ"), False):
    logging.getLogger().setLevel(bstack111111lll1l_opy_)
    return bstack111111lll1l_opy_
  global bstack11111l1l111_opy_
  bstack111lll11l_opy_()
  bstack11111l1ll1l_opy_ = logging.Formatter(
    fmt=bstack11l1111_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬἄ"),
    datefmt=bstack11l1111_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨἅ"),
  )
  bstack11111l11l11_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l1l111_opy_)
  file_handler.setFormatter(bstack11111l1ll1l_opy_)
  bstack11111l11l11_opy_.setFormatter(bstack11111l1ll1l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l11l11_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l1111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡵࡩࡲࡵࡴࡦ࠰ࡵࡩࡲࡵࡴࡦࡡࡦࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭ἆ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l11l11_opy_.setLevel(bstack111111lll1l_opy_)
  logging.getLogger().addHandler(bstack11111l11l11_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111111lll1l_opy_
def bstack111111ll11l_opy_(config):
  try:
    bstack11111l1l1l1_opy_ = set(bstack11l11l1lll1_opy_)
    bstack11111l1lll1_opy_ = bstack11l1111_opy_ (u"ࠬ࠭ἇ")
    with open(bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩἈ")) as bstack111111ll1l1_opy_:
      bstack111111l1lll_opy_ = bstack111111ll1l1_opy_.read()
      bstack11111l1lll1_opy_ = re.sub(bstack11l1111_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠥ࠱࠮ࠩࡢ࡮ࠨἉ"), bstack11l1111_opy_ (u"ࠨࠩἊ"), bstack111111l1lll_opy_, flags=re.M)
      bstack11111l1lll1_opy_ = re.sub(
        bstack11l1111_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠬࠬἋ") + bstack11l1111_opy_ (u"ࠪࢀࠬἌ").join(bstack11111l1l1l1_opy_) + bstack11l1111_opy_ (u"ࠫ࠮࠴ࠪࠥࠩἍ"),
        bstack11l1111_opy_ (u"ࡷ࠭࡜࠳࠼ࠣ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧἎ"),
        bstack11111l1lll1_opy_, flags=re.M | re.I
      )
    def bstack11111l11lll_opy_(dic):
      bstack11111l11ll1_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1l1l1_opy_:
          bstack11111l11ll1_opy_[key] = bstack11l1111_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪἏ")
        else:
          if isinstance(value, dict):
            bstack11111l11ll1_opy_[key] = bstack11111l11lll_opy_(value)
          else:
            bstack11111l11ll1_opy_[key] = value
      return bstack11111l11ll1_opy_
    bstack11111l11ll1_opy_ = bstack11111l11lll_opy_(config)
    return {
      bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪἐ"): bstack11111l1lll1_opy_,
      bstack11l1111_opy_ (u"ࠨࡨ࡬ࡲࡦࡲࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫἑ"): json.dumps(bstack11111l11ll1_opy_)
    }
  except Exception as e:
    return {}
def bstack111111ll1ll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l1111_opy_ (u"ࠩ࡯ࡳ࡬࠭ἒ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l11l1l_opy_ = os.path.join(log_dir, bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶࠫἓ"))
  if not os.path.exists(bstack11111l11l1l_opy_):
    bstack11111l111l1_opy_ = {
      bstack11l1111_opy_ (u"ࠦ࡮ࡴࡩࡱࡣࡷ࡬ࠧἔ"): str(inipath),
      bstack11l1111_opy_ (u"ࠧࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠢἕ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l1111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬ἖")), bstack11l1111_opy_ (u"ࠧࡸࠩ἗")) as bstack11111l1111l_opy_:
      bstack11111l1111l_opy_.write(json.dumps(bstack11111l111l1_opy_))
def bstack11111l111ll_opy_():
  try:
    bstack11111l11l1l_opy_ = os.path.join(os.getcwd(), bstack11l1111_opy_ (u"ࠨ࡮ࡲ࡫ࠬἘ"), bstack11l1111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨἙ"))
    if os.path.exists(bstack11111l11l1l_opy_):
      with open(bstack11111l11l1l_opy_, bstack11l1111_opy_ (u"ࠪࡶࠬἚ")) as bstack11111l1111l_opy_:
        bstack111111ll111_opy_ = json.load(bstack11111l1111l_opy_)
      return bstack111111ll111_opy_.get(bstack11l1111_opy_ (u"ࠫ࡮ࡴࡩࡱࡣࡷ࡬ࠬἛ"), bstack11l1111_opy_ (u"ࠬ࠭Ἔ")), bstack111111ll111_opy_.get(bstack11l1111_opy_ (u"࠭ࡲࡰࡱࡷࡴࡦࡺࡨࠨἝ"), bstack11l1111_opy_ (u"ࠧࠨ἞"))
  except:
    pass
  return None, None
def bstack111111lll11_opy_():
  try:
    bstack11111l11l1l_opy_ = os.path.join(os.getcwd(), bstack11l1111_opy_ (u"ࠨ࡮ࡲ࡫ࠬ἟"), bstack11l1111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨἠ"))
    if os.path.exists(bstack11111l11l1l_opy_):
      os.remove(bstack11111l11l1l_opy_)
  except:
    pass
def bstack11lll11l_opy_(config):
  try:
    from bstack_utils.helper import bstack1llll11ll_opy_, bstack11llll111_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l1l111_opy_
    if config.get(bstack11l1111_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬἡ"), False):
      return
    uuid = os.getenv(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩἢ")) if os.getenv(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪἣ")) else bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣἤ"))
    if not uuid or uuid == bstack11l1111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬἥ"):
      return
    bstack111111lllll_opy_ = [bstack11l1111_opy_ (u"ࠨࡴࡨࡵࡺ࡯ࡲࡦ࡯ࡨࡲࡹࡹ࠮ࡵࡺࡷࠫἦ"), bstack11l1111_opy_ (u"ࠩࡓ࡭ࡵ࡬ࡩ࡭ࡧࠪἧ"), bstack11l1111_opy_ (u"ࠪࡴࡾࡶࡲࡰ࡬ࡨࡧࡹ࠴ࡴࡰ࡯࡯ࠫἨ"), bstack11111l1l111_opy_, bstack11111l1l1ll_opy_]
    bstack11111l1l11l_opy_, root_path = bstack11111l111ll_opy_()
    if bstack11111l1l11l_opy_ != None:
      bstack111111lllll_opy_.append(bstack11111l1l11l_opy_)
    if root_path != None:
      bstack111111lllll_opy_.append(os.path.join(root_path, bstack11l1111_opy_ (u"ࠫࡨࡵ࡮ࡧࡶࡨࡷࡹ࠴ࡰࡺࠩἩ")))
    bstack111lll11l_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡲ࡯ࡨࡵ࠰ࠫἪ") + uuid + bstack11l1111_opy_ (u"࠭࠮ࡵࡣࡵ࠲࡬ࢀࠧἫ"))
    with tarfile.open(output_file, bstack11l1111_opy_ (u"ࠢࡸ࠼ࡪࡾࠧἬ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111111lllll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111111ll11l_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1ll11_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1ll11_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1ll11_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l1111_opy_ (u"ࠨࡦࡤࡸࡦ࠭Ἥ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l1111_opy_ (u"ࠩࡵࡦࠬἮ")), bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺ࠰࡫ࡿ࡯ࡰࠨἯ")),
        bstack11l1111_opy_ (u"ࠫࡨࡲࡩࡦࡰࡷࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ἰ"): uuid
      }
    )
    bstack11111l11111_opy_ = bstack11llll111_opy_(cli.config, [bstack11l1111_opy_ (u"ࠧࡧࡰࡪࡵࠥἱ"), bstack11l1111_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨἲ"), bstack11l1111_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪࠢἳ")], bstack11l11ll1lll_opy_)
    response = requests.post(
      bstack11l1111_opy_ (u"ࠣࡽࢀ࠳ࡨࡲࡩࡦࡰࡷ࠱ࡱࡵࡧࡴ࠱ࡸࡴࡱࡵࡡࡥࠤἴ").format(bstack11111l11111_opy_),
      data=multipart_data,
      headers={bstack11l1111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨἵ"): multipart_data.content_type},
      auth=(config[bstack11l1111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬἶ")], config[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧἷ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l1111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫἸ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l1111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬἹ") + str(e))
  finally:
    try:
      bstack1ll11111ll1_opy_()
      bstack111111lll11_opy_()
    except:
      pass