# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11l11l_opy_, bstack11l11ll11l1_opy_, bstack11l11l11ll1_opy_
import tempfile
import json
bstack11111l1lll1_opy_ = os.getenv(bstack11111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡍ࡟ࡇࡋࡏࡉࠧỸ"), None) or os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠢỹ"))
bstack111111ll11l_opy_ = os.path.join(bstack11111_opy_ (u"ࠨ࡬ࡰࡩࠥỺ"), bstack11111_opy_ (u"ࠧࡴࡦ࡮࠱ࡨࡲࡩ࠮ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫỻ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11111_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫỼ"),
      datefmt=bstack11111_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧỽ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l11l111l_opy_():
  bstack111111ll1ll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡇࡉࡇ࡛ࡇࠣỾ"), bstack11111_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥỿ"))
  return logging.DEBUG if bstack111111ll1ll_opy_.lower() == bstack11111_opy_ (u"ࠧࡺࡲࡶࡧࠥἀ") else logging.INFO
def bstack1ll11111l11_opy_():
  global bstack11111l1lll1_opy_
  if os.path.exists(bstack11111l1lll1_opy_):
    os.remove(bstack11111l1lll1_opy_)
  if os.path.exists(bstack111111ll11l_opy_):
    os.remove(bstack111111ll11l_opy_)
def bstack1l111l1ll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack111111llll1_opy_ = log_level
  if bstack11111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨἁ") in config and config[bstack11111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩἂ")] in bstack11l11ll11l1_opy_:
    bstack111111llll1_opy_ = bstack11l11ll11l1_opy_[config[bstack11111_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪἃ")]]
  if config.get(bstack11111_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫἄ"), False):
    logging.getLogger().setLevel(bstack111111llll1_opy_)
    return bstack111111llll1_opy_
  global bstack11111l1lll1_opy_
  bstack1l111l1ll_opy_()
  bstack11111l11lll_opy_ = logging.Formatter(
    fmt=bstack11111_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭ἅ"),
    datefmt=bstack11111_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩἆ"),
  )
  bstack11111l111l1_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l1lll1_opy_)
  file_handler.setFormatter(bstack11111l11lll_opy_)
  bstack11111l111l1_opy_.setFormatter(bstack11111l11lll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l111l1_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧἇ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l111l1_opy_.setLevel(bstack111111llll1_opy_)
  logging.getLogger().addHandler(bstack11111l111l1_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111111llll1_opy_
def bstack11111l11l11_opy_(config):
  try:
    bstack11111l1l111_opy_ = set(bstack11l11l11ll1_opy_)
    bstack111111lll11_opy_ = bstack11111_opy_ (u"࠭ࠧἈ")
    with open(bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪἉ")) as bstack111111lll1l_opy_:
      bstack11111l11l1l_opy_ = bstack111111lll1l_opy_.read()
      bstack111111lll11_opy_ = re.sub(bstack11111_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩἊ"), bstack11111_opy_ (u"ࠩࠪἋ"), bstack11111l11l1l_opy_, flags=re.M)
      bstack111111lll11_opy_ = re.sub(
        bstack11111_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭Ἄ") + bstack11111_opy_ (u"ࠫࢁ࠭Ἅ").join(bstack11111l1l111_opy_) + bstack11111_opy_ (u"ࠬ࠯࠮ࠫࠦࠪἎ"),
        bstack11111_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨἏ"),
        bstack111111lll11_opy_, flags=re.M | re.I
      )
    def bstack11111l1llll_opy_(dic):
      bstack111111ll1l1_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1l111_opy_:
          bstack111111ll1l1_opy_[key] = bstack11111_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫἐ")
        else:
          if isinstance(value, dict):
            bstack111111ll1l1_opy_[key] = bstack11111l1llll_opy_(value)
          else:
            bstack111111ll1l1_opy_[key] = value
      return bstack111111ll1l1_opy_
    bstack111111ll1l1_opy_ = bstack11111l1llll_opy_(config)
    return {
      bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫἑ"): bstack111111lll11_opy_,
      bstack11111_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬἒ"): json.dumps(bstack111111ll1l1_opy_)
    }
  except Exception as e:
    return {}
def bstack111111ll111_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠪࡰࡴ࡭ࠧἓ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack111111lllll_opy_ = os.path.join(log_dir, bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷࠬἔ"))
  if not os.path.exists(bstack111111lllll_opy_):
    bstack11111l1111l_opy_ = {
      bstack11111_opy_ (u"ࠧ࡯࡮ࡪࡲࡤࡸ࡭ࠨἕ"): str(inipath),
      bstack11111_opy_ (u"ࠨࡲࡰࡱࡷࡴࡦࡺࡨࠣ἖"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭἗")), bstack11111_opy_ (u"ࠨࡹࠪἘ")) as bstack11111l1l1l1_opy_:
      bstack11111l1l1l1_opy_.write(json.dumps(bstack11111l1111l_opy_))
def bstack11111l11ll1_opy_():
  try:
    bstack111111lllll_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠩ࡯ࡳ࡬࠭Ἑ"), bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩἚ"))
    if os.path.exists(bstack111111lllll_opy_):
      with open(bstack111111lllll_opy_, bstack11111_opy_ (u"ࠫࡷ࠭Ἓ")) as bstack11111l1l1l1_opy_:
        bstack11111l111ll_opy_ = json.load(bstack11111l1l1l1_opy_)
      return bstack11111l111ll_opy_.get(bstack11111_opy_ (u"ࠬ࡯࡮ࡪࡲࡤࡸ࡭࠭Ἔ"), bstack11111_opy_ (u"࠭ࠧἝ")), bstack11111l111ll_opy_.get(bstack11111_opy_ (u"ࠧࡳࡱࡲࡸࡵࡧࡴࡩࠩ἞"), bstack11111_opy_ (u"ࠨࠩ἟"))
  except:
    pass
  return None, None
def bstack11111l1ll11_opy_():
  try:
    bstack111111lllll_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠩ࡯ࡳ࡬࠭ἠ"), bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩἡ"))
    if os.path.exists(bstack111111lllll_opy_):
      os.remove(bstack111111lllll_opy_)
  except:
    pass
def bstack1l11l1ll_opy_(config):
  try:
    from bstack_utils.helper import bstack111lll11_opy_, bstack11ll11l111_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l1lll1_opy_
    if config.get(bstack11111_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ἢ"), False):
      return
    uuid = os.getenv(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪἣ")) if os.getenv(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫἤ")) else bstack111lll11_opy_.get_property(bstack11111_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤἥ"))
    if not uuid or uuid == bstack11111_opy_ (u"ࠨࡰࡸࡰࡱ࠭ἦ"):
      return
    bstack11111l1ll1l_opy_ = [bstack11111_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬἧ"), bstack11111_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫἨ"), bstack11111_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬἩ"), bstack11111l1lll1_opy_, bstack111111ll11l_opy_]
    bstack11111l11111_opy_, root_path = bstack11111l11ll1_opy_()
    if bstack11111l11111_opy_ != None:
      bstack11111l1ll1l_opy_.append(bstack11111l11111_opy_)
    if root_path != None:
      bstack11111l1ll1l_opy_.append(os.path.join(root_path, bstack11111_opy_ (u"ࠬࡩ࡯࡯ࡨࡷࡩࡸࡺ࠮ࡱࡻࠪἪ")))
    bstack1l111l1ll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡬ࡰࡩࡶ࠱ࠬἫ") + uuid + bstack11111_opy_ (u"ࠧ࠯ࡶࡤࡶ࠳࡭ࡺࠨἬ"))
    with tarfile.open(output_file, bstack11111_opy_ (u"ࠣࡹ࠽࡫ࡿࠨἭ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1ll1l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l11l11_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1l1ll_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1l1ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1l1ll_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11111_opy_ (u"ࠩࡧࡥࡹࡧࠧἮ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11111_opy_ (u"ࠪࡶࡧ࠭Ἧ")), bstack11111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࠱࡬ࢀࡩࡱࠩἰ")),
        bstack11111_opy_ (u"ࠬࡩ࡬ࡪࡧࡱࡸࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧἱ"): uuid
      }
    )
    bstack11111l1l11l_opy_ = bstack11ll11l111_opy_(cli.config, [bstack11111_opy_ (u"ࠨࡡࡱ࡫ࡶࠦἲ"), bstack11111_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢἳ"), bstack11111_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࠣἴ")], bstack11l1l11l11l_opy_)
    response = requests.post(
      bstack11111_opy_ (u"ࠤࡾࢁ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥἵ").format(bstack11111l1l11l_opy_),
      data=multipart_data,
      headers={bstack11111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩἶ"): multipart_data.content_type},
      auth=(config[bstack11111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ἷ")], config[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨἸ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬἹ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭Ἲ") + str(e))
  finally:
    try:
      bstack1ll11111l11_opy_()
      bstack11111l1ll11_opy_()
    except:
      pass