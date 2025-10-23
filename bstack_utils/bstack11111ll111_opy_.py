# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l11ll1ll1_opy_, bstack11l1l1lll1l_opy_, bstack11l11llllll_opy_
import tempfile
import json
bstack1111l11111l_opy_ = os.getenv(bstack111111l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡊࡣࡋࡏࡌࡆࠤẚ"), None) or os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡦࡨࡦࡺ࡭࠮࡭ࡱࡪࠦẛ"))
bstack11111llll11_opy_ = os.path.join(bstack111111l_opy_ (u"ࠥࡰࡴ࡭ࠢẜ"), bstack111111l_opy_ (u"ࠫࡸࡪ࡫࠮ࡥ࡯࡭࠲ࡪࡥࡣࡷࡪ࠲ࡱࡵࡧࠨẝ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack111111l_opy_ (u"ࠬࠫࠨࡢࡵࡦࡸ࡮ࡳࡥࠪࡵࠣ࡟ࠪ࠮࡮ࡢ࡯ࡨ࠭ࡸࡣ࡛ࠦࠪ࡯ࡩࡻ࡫࡬࡯ࡣࡰࡩ࠮ࡹ࡝ࠡ࠯ࠣࠩ࠭ࡳࡥࡴࡵࡤ࡫ࡪ࠯ࡳࠨẞ"),
      datefmt=bstack111111l_opy_ (u"࡚࠭ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࡝ࠫẟ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l1lll11l_opy_():
  bstack1111l111111_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡄࡆࡄࡘࡋࠧẠ"), bstack111111l_opy_ (u"ࠣࡨࡤࡰࡸ࡫ࠢạ"))
  return logging.DEBUG if bstack1111l111111_opy_.lower() == bstack111111l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢẢ") else logging.INFO
def bstack1l1llll1lll_opy_():
  global bstack1111l11111l_opy_
  if os.path.exists(bstack1111l11111l_opy_):
    os.remove(bstack1111l11111l_opy_)
  if os.path.exists(bstack11111llll11_opy_):
    os.remove(bstack11111llll11_opy_)
def bstack1l1l1l1111_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111llllll_opy_ = log_level
  if bstack111111l_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬả") in config and config[bstack111111l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭Ấ")] in bstack11l1l1lll1l_opy_:
    bstack11111llllll_opy_ = bstack11l1l1lll1l_opy_[config[bstack111111l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧấ")]]
  if config.get(bstack111111l_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨẦ"), False):
    logging.getLogger().setLevel(bstack11111llllll_opy_)
    return bstack11111llllll_opy_
  global bstack1111l11111l_opy_
  bstack1l1l1l1111_opy_()
  bstack11111lll1ll_opy_ = logging.Formatter(
    fmt=bstack111111l_opy_ (u"ࠧࠦࠪࡤࡷࡨࡺࡩ࡮ࡧࠬࡷࠥࡡࠥࠩࡰࡤࡱࡪ࠯ࡳ࡞࡝ࠨࠬࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠩࡴ࡟ࠣ࠱ࠥࠫࠨ࡮ࡧࡶࡷࡦ࡭ࡥࠪࡵࠪầ"),
    datefmt=bstack111111l_opy_ (u"ࠨࠧ࡜࠱ࠪࡳ࠭ࠦࡦࡗࠩࡍࡀࠥࡎ࠼ࠨࡗ࡟࠭Ẩ"),
  )
  bstack11111ll1l11_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack1111l11111l_opy_)
  file_handler.setFormatter(bstack11111lll1ll_opy_)
  bstack11111ll1l11_opy_.setFormatter(bstack11111lll1ll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll1l11_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack111111l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡳࡧࡰࡳࡹ࡫࠮ࡳࡧࡰࡳࡹ࡫࡟ࡤࡱࡱࡲࡪࡩࡴࡪࡱࡱࠫẩ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll1l11_opy_.setLevel(bstack11111llllll_opy_)
  logging.getLogger().addHandler(bstack11111ll1l11_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111llllll_opy_
def bstack11111l1l1ll_opy_(config):
  try:
    bstack11111ll111l_opy_ = set(bstack11l11llllll_opy_)
    bstack11111ll11l1_opy_ = bstack111111l_opy_ (u"ࠪࠫẪ")
    with open(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧẫ")) as bstack11111l1llll_opy_:
      bstack11111l1ll1l_opy_ = bstack11111l1llll_opy_.read()
      bstack11111ll11l1_opy_ = re.sub(bstack111111l_opy_ (u"ࡷ࠭࡞ࠩ࡞ࡶ࠯࠮ࡅࠣ࠯ࠬࠧࡠࡳ࠭Ậ"), bstack111111l_opy_ (u"࠭ࠧậ"), bstack11111l1ll1l_opy_, flags=re.M)
      bstack11111ll11l1_opy_ = re.sub(
        bstack111111l_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠪࠪẮ") + bstack111111l_opy_ (u"ࠨࡾࠪắ").join(bstack11111ll111l_opy_) + bstack111111l_opy_ (u"ࠩࠬ࠲࠯ࠪࠧẰ"),
        bstack111111l_opy_ (u"ࡵࠫࡡ࠸࠺ࠡ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬằ"),
        bstack11111ll11l1_opy_, flags=re.M | re.I
      )
    def bstack11111lll1l1_opy_(dic):
      bstack11111ll11ll_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111ll111l_opy_:
          bstack11111ll11ll_opy_[key] = bstack111111l_opy_ (u"ࠫࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨẲ")
        else:
          if isinstance(value, dict):
            bstack11111ll11ll_opy_[key] = bstack11111lll1l1_opy_(value)
          else:
            bstack11111ll11ll_opy_[key] = value
      return bstack11111ll11ll_opy_
    bstack11111ll11ll_opy_ = bstack11111lll1l1_opy_(config)
    return {
      bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨẳ"): bstack11111ll11l1_opy_,
      bstack111111l_opy_ (u"࠭ࡦࡪࡰࡤࡰࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩẴ"): json.dumps(bstack11111ll11ll_opy_)
    }
  except Exception as e:
    return {}
def bstack1111l1111l1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack111111l_opy_ (u"ࠧ࡭ࡱࡪࠫẵ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll1l1l_opy_ = os.path.join(log_dir, bstack111111l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴࠩẶ"))
  if not os.path.exists(bstack11111ll1l1l_opy_):
    bstack11111llll1l_opy_ = {
      bstack111111l_opy_ (u"ࠤ࡬ࡲ࡮ࡶࡡࡵࡪࠥặ"): str(inipath),
      bstack111111l_opy_ (u"ࠥࡶࡴࡵࡴࡱࡣࡷ࡬ࠧẸ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡨࡵ࡮ࡧ࡫ࡪࡷ࠳ࡰࡳࡰࡰࠪẹ")), bstack111111l_opy_ (u"ࠬࡽࠧẺ")) as bstack11111lll111_opy_:
      bstack11111lll111_opy_.write(json.dumps(bstack11111llll1l_opy_))
def bstack11111ll1111_opy_():
  try:
    bstack11111ll1l1l_opy_ = os.path.join(os.getcwd(), bstack111111l_opy_ (u"࠭࡬ࡰࡩࠪẻ"), bstack111111l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭Ẽ"))
    if os.path.exists(bstack11111ll1l1l_opy_):
      with open(bstack11111ll1l1l_opy_, bstack111111l_opy_ (u"ࠨࡴࠪẽ")) as bstack11111lll111_opy_:
        bstack11111lll11l_opy_ = json.load(bstack11111lll111_opy_)
      return bstack11111lll11l_opy_.get(bstack111111l_opy_ (u"ࠩ࡬ࡲ࡮ࡶࡡࡵࡪࠪẾ"), bstack111111l_opy_ (u"ࠪࠫế")), bstack11111lll11l_opy_.get(bstack111111l_opy_ (u"ࠫࡷࡵ࡯ࡵࡲࡤࡸ࡭࠭Ề"), bstack111111l_opy_ (u"ࠬ࠭ề"))
  except:
    pass
  return None, None
def bstack11111l1lll1_opy_():
  try:
    bstack11111ll1l1l_opy_ = os.path.join(os.getcwd(), bstack111111l_opy_ (u"࠭࡬ࡰࡩࠪỂ"), bstack111111l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡤࡱࡱࡪ࡮࡭ࡳ࠯࡬ࡶࡳࡳ࠭ể"))
    if os.path.exists(bstack11111ll1l1l_opy_):
      os.remove(bstack11111ll1l1l_opy_)
  except:
    pass
def bstack1l11l1l1_opy_(config):
  try:
    from bstack_utils.helper import bstack11111lll_opy_, bstack1lll1111l_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack1111l11111l_opy_
    if config.get(bstack111111l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪỄ"), False):
      return
    uuid = os.getenv(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧễ")) if os.getenv(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨỆ")) else bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨệ"))
    if not uuid or uuid == bstack111111l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪỈ"):
      return
    bstack11111ll1ll1_opy_ = [bstack111111l_opy_ (u"࠭ࡲࡦࡳࡸ࡭ࡷ࡫࡭ࡦࡰࡷࡷ࠳ࡺࡸࡵࠩỉ"), bstack111111l_opy_ (u"ࠧࡑ࡫ࡳࡪ࡮ࡲࡥࠨỊ"), bstack111111l_opy_ (u"ࠨࡲࡼࡴࡷࡵࡪࡦࡥࡷ࠲ࡹࡵ࡭࡭ࠩị"), bstack1111l11111l_opy_, bstack11111llll11_opy_]
    bstack11111ll1lll_opy_, root_path = bstack11111ll1111_opy_()
    if bstack11111ll1lll_opy_ != None:
      bstack11111ll1ll1_opy_.append(bstack11111ll1lll_opy_)
    if root_path != None:
      bstack11111ll1ll1_opy_.append(os.path.join(root_path, bstack111111l_opy_ (u"ࠩࡦࡳࡳ࡬ࡴࡦࡵࡷ࠲ࡵࡿࠧỌ")))
    bstack1l1l1l1111_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡰࡴ࡭ࡳ࠮ࠩọ") + uuid + bstack111111l_opy_ (u"ࠫ࠳ࡺࡡࡳ࠰ࡪࡾࠬỎ"))
    with tarfile.open(output_file, bstack111111l_opy_ (u"ࠧࡽ࠺ࡨࡼࠥỏ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111ll1ll1_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l1l1ll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1ll11_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1ll11_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1ll11_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack111111l_opy_ (u"࠭ࡤࡢࡶࡤࠫỐ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack111111l_opy_ (u"ࠧࡳࡤࠪố")), bstack111111l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡸ࠮ࡩࡽ࡭ࡵ࠭Ồ")),
        bstack111111l_opy_ (u"ࠩࡦࡰ࡮࡫࡮ࡵࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫồ"): uuid
      }
    )
    bstack11111lllll1_opy_ = bstack1lll1111l_opy_(cli.config, [bstack111111l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣỔ"), bstack111111l_opy_ (u"ࠦࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠦổ"), bstack111111l_opy_ (u"ࠧࡻࡰ࡭ࡱࡤࡨࠧỖ")], bstack11l11ll1ll1_opy_)
    response = requests.post(
      bstack111111l_opy_ (u"ࠨࡻࡾ࠱ࡦࡰ࡮࡫࡮ࡵ࠯࡯ࡳ࡬ࡹ࠯ࡶࡲ࡯ࡳࡦࡪࠢỗ").format(bstack11111lllll1_opy_),
      data=multipart_data,
      headers={bstack111111l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭Ộ"): multipart_data.content_type},
      auth=(config[bstack111111l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪộ")], config[bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬỚ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack111111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡸࡴࡱࡵࡡࡥࠢ࡯ࡳ࡬ࡹ࠺ࠡࠩớ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack111111l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡴࡤࡪࡰࡪࠤࡱࡵࡧࡴ࠼ࠪỜ") + str(e))
  finally:
    try:
      bstack1l1llll1lll_opy_()
      bstack11111l1lll1_opy_()
    except:
      pass