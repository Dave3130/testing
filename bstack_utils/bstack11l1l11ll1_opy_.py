# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11l1ll11_opy_, bstack11l1l11lll1_opy_, bstack11l11ll1ll1_opy_
import tempfile
import json
bstack11111l11l1l_opy_ = os.getenv(bstack11l11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡌࡥࡆࡊࡎࡈࠦỢ"), None) or os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬ࠨợ"))
bstack11111l11111_opy_ = os.path.join(bstack11l11ll_opy_ (u"ࠧࡲ࡯ࡨࠤỤ"), bstack11l11ll_opy_ (u"࠭ࡳࡥ࡭࠰ࡧࡱ࡯࠭ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪụ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11l11ll_opy_ (u"ࠧࠦࠪࡤࡷࡨࡺࡩ࡮ࡧࠬࡷࠥࡡࠥࠩࡰࡤࡱࡪ࠯ࡳ࡞࡝ࠨࠬࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠩࡴ࡟ࠣ࠱ࠥࠫࠨ࡮ࡧࡶࡷࡦ࡭ࡥࠪࡵࠪỦ"),
      datefmt=bstack11l11ll_opy_ (u"ࠨࠧ࡜࠱ࠪࡳ࠭ࠦࡦࡗࠩࡍࡀࠥࡎ࠼ࠨࡗ࡟࠭ủ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l11llll1_opy_():
  bstack11111l1111l_opy_ = os.environ.get(bstack11l11ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡆࡈࡆ࡚ࡍࠢỨ"), bstack11l11ll_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤứ"))
  return logging.DEBUG if bstack11111l1111l_opy_.lower() == bstack11l11ll_opy_ (u"ࠦࡹࡸࡵࡦࠤỪ") else logging.INFO
def bstack1ll11ll11ll_opy_():
  global bstack11111l11l1l_opy_
  if os.path.exists(bstack11111l11l1l_opy_):
    os.remove(bstack11111l11l1l_opy_)
  if os.path.exists(bstack11111l11111_opy_):
    os.remove(bstack11111l11111_opy_)
def bstack11l1l1l11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1lll1_opy_ = log_level
  if bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧừ") in config and config[bstack11l11ll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨỬ")] in bstack11l1l11lll1_opy_:
    bstack11111l1lll1_opy_ = bstack11l1l11lll1_opy_[config[bstack11l11ll_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩử")]]
  if config.get(bstack11l11ll_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪỮ"), False):
    logging.getLogger().setLevel(bstack11111l1lll1_opy_)
    return bstack11111l1lll1_opy_
  global bstack11111l11l1l_opy_
  bstack11l1l1l11_opy_()
  bstack11111l11l11_opy_ = logging.Formatter(
    fmt=bstack11l11ll_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬữ"),
    datefmt=bstack11l11ll_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨỰ"),
  )
  bstack11111l1ll1l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111l11l1l_opy_)
  file_handler.setFormatter(bstack11111l11l11_opy_)
  bstack11111l1ll1l_opy_.setFormatter(bstack11111l11l11_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l1ll1l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11l11ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡵࡩࡲࡵࡴࡦ࠰ࡵࡩࡲࡵࡴࡦࡡࡦࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭ự"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l1ll1l_opy_.setLevel(bstack11111l1lll1_opy_)
  logging.getLogger().addHandler(bstack11111l1ll1l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1lll1_opy_
def bstack11111l1l1ll_opy_(config):
  try:
    bstack11111ll11l1_opy_ = set(bstack11l11ll1ll1_opy_)
    bstack11111ll1111_opy_ = bstack11l11ll_opy_ (u"ࠬ࠭Ỳ")
    with open(bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩỳ")) as bstack11111ll1l11_opy_:
      bstack11111l11ll1_opy_ = bstack11111ll1l11_opy_.read()
      bstack11111ll1111_opy_ = re.sub(bstack11l11ll_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠥ࠱࠮ࠩࡢ࡮ࠨỴ"), bstack11l11ll_opy_ (u"ࠨࠩỵ"), bstack11111l11ll1_opy_, flags=re.M)
      bstack11111ll1111_opy_ = re.sub(
        bstack11l11ll_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠬࠬỶ") + bstack11l11ll_opy_ (u"ࠪࢀࠬỷ").join(bstack11111ll11l1_opy_) + bstack11l11ll_opy_ (u"ࠫ࠮࠴ࠪࠥࠩỸ"),
        bstack11l11ll_opy_ (u"ࡷ࠭࡜࠳࠼ࠣ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧỹ"),
        bstack11111ll1111_opy_, flags=re.M | re.I
      )
    def bstack11111l111l1_opy_(dic):
      bstack11111ll11ll_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111ll11l1_opy_:
          bstack11111ll11ll_opy_[key] = bstack11l11ll_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪỺ")
        else:
          if isinstance(value, dict):
            bstack11111ll11ll_opy_[key] = bstack11111l111l1_opy_(value)
          else:
            bstack11111ll11ll_opy_[key] = value
      return bstack11111ll11ll_opy_
    bstack11111ll11ll_opy_ = bstack11111l111l1_opy_(config)
    return {
      bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪỻ"): bstack11111ll1111_opy_,
      bstack11l11ll_opy_ (u"ࠨࡨ࡬ࡲࡦࡲࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫỼ"): json.dumps(bstack11111ll11ll_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l11lll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11l11ll_opy_ (u"ࠩ࡯ࡳ࡬࠭ỽ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1l111_opy_ = os.path.join(log_dir, bstack11l11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶࠫỾ"))
  if not os.path.exists(bstack11111l1l111_opy_):
    bstack11111l1ll11_opy_ = {
      bstack11l11ll_opy_ (u"ࠦ࡮ࡴࡩࡱࡣࡷ࡬ࠧỿ"): str(inipath),
      bstack11l11ll_opy_ (u"ࠧࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠢἀ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11l11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬἁ")), bstack11l11ll_opy_ (u"ࠧࡸࠩἂ")) as bstack111111llll1_opy_:
      bstack111111llll1_opy_.write(json.dumps(bstack11111l1ll11_opy_))
def bstack11111ll111l_opy_():
  try:
    bstack11111l1l111_opy_ = os.path.join(os.getcwd(), bstack11l11ll_opy_ (u"ࠨ࡮ࡲ࡫ࠬἃ"), bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨἄ"))
    if os.path.exists(bstack11111l1l111_opy_):
      with open(bstack11111l1l111_opy_, bstack11l11ll_opy_ (u"ࠪࡶࠬἅ")) as bstack111111llll1_opy_:
        bstack11111l1l1l1_opy_ = json.load(bstack111111llll1_opy_)
      return bstack11111l1l1l1_opy_.get(bstack11l11ll_opy_ (u"ࠫ࡮ࡴࡩࡱࡣࡷ࡬ࠬἆ"), bstack11l11ll_opy_ (u"ࠬ࠭ἇ")), bstack11111l1l1l1_opy_.get(bstack11l11ll_opy_ (u"࠭ࡲࡰࡱࡷࡴࡦࡺࡨࠨἈ"), bstack11l11ll_opy_ (u"ࠧࠨἉ"))
  except:
    pass
  return None, None
def bstack111111lll1l_opy_():
  try:
    bstack11111l1l111_opy_ = os.path.join(os.getcwd(), bstack11l11ll_opy_ (u"ࠨ࡮ࡲ࡫ࠬἊ"), bstack11l11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨἋ"))
    if os.path.exists(bstack11111l1l111_opy_):
      os.remove(bstack11111l1l111_opy_)
  except:
    pass
def bstack1ll1l111_opy_(config):
  try:
    from bstack_utils.helper import bstack1lll11111_opy_, bstack11111l111l_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111l11l1l_opy_
    if config.get(bstack11l11ll_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬἌ"), False):
      return
    uuid = os.getenv(bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩἍ")) if os.getenv(bstack11l11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪἎ")) else bstack1lll11111_opy_.get_property(bstack11l11ll_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣἏ"))
    if not uuid or uuid == bstack11l11ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬἐ"):
      return
    bstack111111lllll_opy_ = [bstack11l11ll_opy_ (u"ࠨࡴࡨࡵࡺ࡯ࡲࡦ࡯ࡨࡲࡹࡹ࠮ࡵࡺࡷࠫἑ"), bstack11l11ll_opy_ (u"ࠩࡓ࡭ࡵ࡬ࡩ࡭ࡧࠪἒ"), bstack11l11ll_opy_ (u"ࠪࡴࡾࡶࡲࡰ࡬ࡨࡧࡹ࠴ࡴࡰ࡯࡯ࠫἓ"), bstack11111l11l1l_opy_, bstack11111l11111_opy_]
    bstack11111l1llll_opy_, root_path = bstack11111ll111l_opy_()
    if bstack11111l1llll_opy_ != None:
      bstack111111lllll_opy_.append(bstack11111l1llll_opy_)
    if root_path != None:
      bstack111111lllll_opy_.append(os.path.join(root_path, bstack11l11ll_opy_ (u"ࠫࡨࡵ࡮ࡧࡶࡨࡷࡹ࠴ࡰࡺࠩἔ")))
    bstack11l1l1l11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11l11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡲ࡯ࡨࡵ࠰ࠫἕ") + uuid + bstack11l11ll_opy_ (u"࠭࠮ࡵࡣࡵ࠲࡬ࢀࠧ἖"))
    with tarfile.open(output_file, bstack11l11ll_opy_ (u"ࠢࡸ࠼ࡪࡾࠧ἗")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111111lllll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1l1ll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1l11l_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1l11l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1l11l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11l11ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭Ἐ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11l11ll_opy_ (u"ࠩࡵࡦࠬἙ")), bstack11l11ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺ࠰࡫ࡿ࡯ࡰࠨἚ")),
        bstack11l11ll_opy_ (u"ࠫࡨࡲࡩࡦࡰࡷࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ἓ"): uuid
      }
    )
    bstack11111l111ll_opy_ = bstack11111l111l_opy_(cli.config, [bstack11l11ll_opy_ (u"ࠧࡧࡰࡪࡵࠥἜ"), bstack11l11ll_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨἝ"), bstack11l11ll_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪࠢ἞")], bstack11l11l1ll11_opy_)
    response = requests.post(
      bstack11l11ll_opy_ (u"ࠣࡽࢀ࠳ࡨࡲࡩࡦࡰࡷ࠱ࡱࡵࡧࡴ࠱ࡸࡴࡱࡵࡡࡥࠤ἟").format(bstack11111l111ll_opy_),
      data=multipart_data,
      headers={bstack11l11ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨἠ"): multipart_data.content_type},
      auth=(config[bstack11l11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬἡ")], config[bstack11l11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧἢ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11l11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫἣ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11l11ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬἤ") + str(e))
  finally:
    try:
      bstack1ll11ll11ll_opy_()
      bstack111111lll1l_opy_()
    except:
      pass