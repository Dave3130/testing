# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11lll111_opy_, bstack11l11l1l1l1_opy_, bstack11l11l1l111_opy_
import tempfile
import json
bstack11111ll11ll_opy_ = os.getenv(bstack11ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡍ࡟ࡇࡋࡏࡉࠧợ"), None) or os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡩ࡫ࡢࡶࡩ࠱ࡰࡴ࡭ࠢỤ"))
bstack11111l1l11l_opy_ = os.path.join(bstack11ll1l_opy_ (u"ࠨ࡬ࡰࡩࠥụ"), bstack11ll1l_opy_ (u"ࠧࡴࡦ࡮࠱ࡨࡲࡩ࠮ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠫỦ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11ll1l_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫủ"),
      datefmt=bstack11ll1l_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧỨ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1llll11_opy_():
  bstack11111l11l1l_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡇࡉࡇ࡛ࡇࠣứ"), bstack11ll1l_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥỪ"))
  return logging.DEBUG if bstack11111l11l1l_opy_.lower() == bstack11ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥừ") else logging.INFO
def bstack1l1lllll1l1_opy_():
  global bstack11111ll11ll_opy_
  if os.path.exists(bstack11111ll11ll_opy_):
    os.remove(bstack11111ll11ll_opy_)
  if os.path.exists(bstack11111l1l11l_opy_):
    os.remove(bstack11111l1l11l_opy_)
def bstack1l1111ll11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack111111lll1l_opy_ = log_level
  if bstack11ll1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨỬ") in config and config[bstack11ll1l_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩử")] in bstack11l11l1l1l1_opy_:
    bstack111111lll1l_opy_ = bstack11l11l1l1l1_opy_[config[bstack11ll1l_opy_ (u"ࠨ࡮ࡲ࡫ࡑ࡫ࡶࡦ࡮ࠪỮ")]]
  if config.get(bstack11ll1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫữ"), False):
    logging.getLogger().setLevel(bstack111111lll1l_opy_)
    return bstack111111lll1l_opy_
  global bstack11111ll11ll_opy_
  bstack1l1111ll11_opy_()
  bstack111111lllll_opy_ = logging.Formatter(
    fmt=bstack11ll1l_opy_ (u"ࠪࠩ࠭ࡧࡳࡤࡶ࡬ࡱࡪ࠯ࡳࠡ࡝ࠨࠬࡳࡧ࡭ࡦࠫࡶࡡࡠࠫࠨ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠬࡷࡢࠦ࠭ࠡࠧࠫࡱࡪࡹࡳࡢࡩࡨ࠭ࡸ࠭Ự"),
    datefmt=bstack11ll1l_opy_ (u"ࠫࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࡛ࠩự"),
  )
  bstack11111ll1111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111ll11ll_opy_)
  file_handler.setFormatter(bstack111111lllll_opy_)
  bstack11111ll1111_opy_.setFormatter(bstack111111lllll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll1111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11ll1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡶࡪࡳ࡯ࡵࡧ࠱ࡶࡪࡳ࡯ࡵࡧࡢࡧࡴࡴ࡮ࡦࡥࡷ࡭ࡴࡴࠧỲ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll1111_opy_.setLevel(bstack111111lll1l_opy_)
  logging.getLogger().addHandler(bstack11111ll1111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111111lll1l_opy_
def bstack11111l1ll11_opy_(config):
  try:
    bstack11111l111l1_opy_ = set(bstack11l11l1l111_opy_)
    bstack11111l1l111_opy_ = bstack11ll1l_opy_ (u"࠭ࠧỳ")
    with open(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪỴ")) as bstack111111llll1_opy_:
      bstack11111l11lll_opy_ = bstack111111llll1_opy_.read()
      bstack11111l1l111_opy_ = re.sub(bstack11ll1l_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠦ࠲࠯ࠪ࡜࡯ࠩỵ"), bstack11ll1l_opy_ (u"ࠩࠪỶ"), bstack11111l11lll_opy_, flags=re.M)
      bstack11111l1l111_opy_ = re.sub(
        bstack11ll1l_opy_ (u"ࡵࠫࡣ࠮࡜ࡴ࠭ࠬࡃ࠭࠭ỷ") + bstack11ll1l_opy_ (u"ࠫࢁ࠭Ỹ").join(bstack11111l111l1_opy_) + bstack11ll1l_opy_ (u"ࠬ࠯࠮ࠫࠦࠪỹ"),
        bstack11ll1l_opy_ (u"ࡸࠧ࡝࠴࠽ࠤࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨỺ"),
        bstack11111l1l111_opy_, flags=re.M | re.I
      )
    def bstack11111l11111_opy_(dic):
      bstack11111l1111l_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l111l1_opy_:
          bstack11111l1111l_opy_[key] = bstack11ll1l_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫỻ")
        else:
          if isinstance(value, dict):
            bstack11111l1111l_opy_[key] = bstack11111l11111_opy_(value)
          else:
            bstack11111l1111l_opy_[key] = value
      return bstack11111l1111l_opy_
    bstack11111l1111l_opy_ = bstack11111l11111_opy_(config)
    return {
      bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫỼ"): bstack11111l1l111_opy_,
      bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡳࡧ࡬ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬỽ"): json.dumps(bstack11111l1111l_opy_)
    }
  except Exception as e:
    return {}
def bstack11111ll11l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠪࡰࡴ࡭ࠧỾ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll111l_opy_ = os.path.join(log_dir, bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷࠬỿ"))
  if not os.path.exists(bstack11111ll111l_opy_):
    bstack11111l1l1l1_opy_ = {
      bstack11ll1l_opy_ (u"ࠧ࡯࡮ࡪࡲࡤࡸ࡭ࠨἀ"): str(inipath),
      bstack11ll1l_opy_ (u"ࠨࡲࡰࡱࡷࡴࡦࡺࡨࠣἁ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭ἂ")), bstack11ll1l_opy_ (u"ࠨࡹࠪἃ")) as bstack11111l1ll1l_opy_:
      bstack11111l1ll1l_opy_.write(json.dumps(bstack11111l1l1l1_opy_))
def bstack11111l111ll_opy_():
  try:
    bstack11111ll111l_opy_ = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠩ࡯ࡳ࡬࠭ἄ"), bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩἅ"))
    if os.path.exists(bstack11111ll111l_opy_):
      with open(bstack11111ll111l_opy_, bstack11ll1l_opy_ (u"ࠫࡷ࠭ἆ")) as bstack11111l1ll1l_opy_:
        bstack11111ll1l11_opy_ = json.load(bstack11111l1ll1l_opy_)
      return bstack11111ll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡪࡲࡤࡸ࡭࠭ἇ"), bstack11ll1l_opy_ (u"࠭ࠧἈ")), bstack11111ll1l11_opy_.get(bstack11ll1l_opy_ (u"ࠧࡳࡱࡲࡸࡵࡧࡴࡩࠩἉ"), bstack11ll1l_opy_ (u"ࠨࠩἊ"))
  except:
    pass
  return None, None
def bstack11111l1l1ll_opy_():
  try:
    bstack11111ll111l_opy_ = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠩ࡯ࡳ࡬࠭Ἃ"), bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶ࠲࡯ࡹ࡯࡯ࠩἌ"))
    if os.path.exists(bstack11111ll111l_opy_):
      os.remove(bstack11111ll111l_opy_)
  except:
    pass
def bstack1lll1ll1_opy_(config):
  try:
    from bstack_utils.helper import bstack111ll1l1_opy_, bstack1lll1l11l1_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111ll11ll_opy_
    if config.get(bstack11ll1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭Ἅ"), False):
      return
    uuid = os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪἎ")) if os.getenv(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫἏ")) else bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤἐ"))
    if not uuid or uuid == bstack11ll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ἑ"):
      return
    bstack11111l11ll1_opy_ = [bstack11ll1l_opy_ (u"ࠩࡵࡩࡶࡻࡩࡳࡧࡰࡩࡳࡺࡳ࠯ࡶࡻࡸࠬἒ"), bstack11ll1l_opy_ (u"ࠪࡔ࡮ࡶࡦࡪ࡮ࡨࠫἓ"), bstack11ll1l_opy_ (u"ࠫࡵࡿࡰࡳࡱ࡭ࡩࡨࡺ࠮ࡵࡱࡰࡰࠬἔ"), bstack11111ll11ll_opy_, bstack11111l1l11l_opy_]
    bstack11111l1llll_opy_, root_path = bstack11111l111ll_opy_()
    if bstack11111l1llll_opy_ != None:
      bstack11111l11ll1_opy_.append(bstack11111l1llll_opy_)
    if root_path != None:
      bstack11111l11ll1_opy_.append(os.path.join(root_path, bstack11ll1l_opy_ (u"ࠬࡩ࡯࡯ࡨࡷࡩࡸࡺ࠮ࡱࡻࠪἕ")))
    bstack1l1111ll11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡬ࡰࡩࡶ࠱ࠬ἖") + uuid + bstack11ll1l_opy_ (u"ࠧ࠯ࡶࡤࡶ࠳࡭ࡺࠨ἗"))
    with tarfile.open(output_file, bstack11ll1l_opy_ (u"ࠣࡹ࠽࡫ࡿࠨἘ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l11ll1_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1ll11_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l11l11_opy_ = data.encode()
        tarinfo.size = len(bstack11111l11l11_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l11l11_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧἙ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11ll1l_opy_ (u"ࠪࡶࡧ࠭Ἒ")), bstack11ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱ࡻ࠱࡬ࢀࡩࡱࠩἛ")),
        bstack11ll1l_opy_ (u"ࠬࡩ࡬ࡪࡧࡱࡸࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧἜ"): uuid
      }
    )
    bstack11111l1lll1_opy_ = bstack1lll1l11l1_opy_(cli.config, [bstack11ll1l_opy_ (u"ࠨࡡࡱ࡫ࡶࠦἝ"), bstack11ll1l_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ἞"), bstack11ll1l_opy_ (u"ࠣࡷࡳࡰࡴࡧࡤࠣ἟")], bstack11l11lll111_opy_)
    response = requests.post(
      bstack11ll1l_opy_ (u"ࠤࡾࢁ࠴ࡩ࡬ࡪࡧࡱࡸ࠲ࡲ࡯ࡨࡵ࠲ࡹࡵࡲ࡯ࡢࡦࠥἠ").format(bstack11111l1lll1_opy_),
      data=multipart_data,
      headers={bstack11ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩἡ"): multipart_data.content_type},
      auth=(config[bstack11ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ἢ")], config[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨἣ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰ࡭ࡱࡤࡨࠥࡲ࡯ࡨࡵ࠽ࠤࠬἤ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11ll1l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠ࡭ࡱࡪࡷ࠿࠭ἥ") + str(e))
  finally:
    try:
      bstack1l1lllll1l1_opy_()
      bstack11111l1l1ll_opy_()
    except:
      pass