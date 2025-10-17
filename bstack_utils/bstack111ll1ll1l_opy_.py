# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l111111_opy_, bstack11l1l1l1lll_opy_, bstack11l1l1ll11l_opy_
import tempfile
import json
bstack11111lll1l1_opy_ = os.getenv(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡌࡥࡆࡊࡎࡈࠦẕ"), None) or os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡨࡪࡨࡵࡨ࠰࡯ࡳ࡬ࠨẖ"))
bstack11111ll11l1_opy_ = os.path.join(bstack11111_opy_ (u"ࠧࡲ࡯ࡨࠤẗ"), bstack11111_opy_ (u"࠭ࡳࡥ࡭࠰ࡧࡱ࡯࠭ࡥࡧࡥࡹ࡬࠴࡬ࡰࡩࠪẘ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack11111_opy_ (u"ࠧࠦࠪࡤࡷࡨࡺࡩ࡮ࡧࠬࡷࠥࡡࠥࠩࡰࡤࡱࡪ࠯ࡳ࡞࡝ࠨࠬࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠩࡴ࡟ࠣ࠱ࠥࠫࠨ࡮ࡧࡶࡷࡦ࡭ࡥࠪࡵࠪẙ"),
      datefmt=bstack11111_opy_ (u"ࠨࠧ࡜࠱ࠪࡳ࠭ࠦࡦࡗࠩࡍࡀࠥࡎ࠼ࠨࡗ࡟࠭ẚ"),
      stream=sys.stdout
    )
  return logger
def bstack1l11lllll1l_opy_():
  bstack11111ll1lll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡆࡈࡆ࡚ࡍࠢẛ"), bstack11111_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤẜ"))
  return logging.DEBUG if bstack11111ll1lll_opy_.lower() == bstack11111_opy_ (u"ࠦࡹࡸࡵࡦࠤẝ") else logging.INFO
def bstack1ll111l11l1_opy_():
  global bstack11111lll1l1_opy_
  if os.path.exists(bstack11111lll1l1_opy_):
    os.remove(bstack11111lll1l1_opy_)
  if os.path.exists(bstack11111ll11l1_opy_):
    os.remove(bstack11111ll11l1_opy_)
def bstack1l111lll11_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1lll1_opy_ = log_level
  if bstack11111_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧẞ") in config and config[bstack11111_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨẟ")] in bstack11l1l1l1lll_opy_:
    bstack11111l1lll1_opy_ = bstack11l1l1l1lll_opy_[config[bstack11111_opy_ (u"ࠧ࡭ࡱࡪࡐࡪࡼࡥ࡭ࠩẠ")]]
  if config.get(bstack11111_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪạ"), False):
    logging.getLogger().setLevel(bstack11111l1lll1_opy_)
    return bstack11111l1lll1_opy_
  global bstack11111lll1l1_opy_
  bstack1l111lll11_opy_()
  bstack11111ll111l_opy_ = logging.Formatter(
    fmt=bstack11111_opy_ (u"ࠩࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬẢ"),
    datefmt=bstack11111_opy_ (u"ࠪࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙࡚ࠪࠨả"),
  )
  bstack11111ll1111_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111lll1l1_opy_)
  file_handler.setFormatter(bstack11111ll111l_opy_)
  bstack11111ll1111_opy_.setFormatter(bstack11111ll111l_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll1111_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack11111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡵࡩࡲࡵࡴࡦ࠰ࡵࡩࡲࡵࡴࡦࡡࡦࡳࡳࡴࡥࡤࡶ࡬ࡳࡳ࠭Ấ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll1111_opy_.setLevel(bstack11111l1lll1_opy_)
  logging.getLogger().addHandler(bstack11111ll1111_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1lll1_opy_
def bstack11111ll1ll1_opy_(config):
  try:
    bstack11111l1l11l_opy_ = set(bstack11l1l1ll11l_opy_)
    bstack11111l1ll11_opy_ = bstack11111_opy_ (u"ࠬ࠭ấ")
    with open(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩẦ")) as bstack11111l1l1ll_opy_:
      bstack11111ll11ll_opy_ = bstack11111l1l1ll_opy_.read()
      bstack11111l1ll11_opy_ = re.sub(bstack11111_opy_ (u"ࡲࠨࡠࠫࡠࡸ࠱ࠩࡀࠥ࠱࠮ࠩࡢ࡮ࠨầ"), bstack11111_opy_ (u"ࠨࠩẨ"), bstack11111ll11ll_opy_, flags=re.M)
      bstack11111l1ll11_opy_ = re.sub(
        bstack11111_opy_ (u"ࡴࠪࡢ࠭ࡢࡳࠬࠫࡂࠬࠬẩ") + bstack11111_opy_ (u"ࠪࢀࠬẪ").join(bstack11111l1l11l_opy_) + bstack11111_opy_ (u"ࠫ࠮࠴ࠪࠥࠩẫ"),
        bstack11111_opy_ (u"ࡷ࠭࡜࠳࠼ࠣ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧẬ"),
        bstack11111l1ll11_opy_, flags=re.M | re.I
      )
    def bstack11111llll11_opy_(dic):
      bstack11111lll11l_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1l11l_opy_:
          bstack11111lll11l_opy_[key] = bstack11111_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪậ")
        else:
          if isinstance(value, dict):
            bstack11111lll11l_opy_[key] = bstack11111llll11_opy_(value)
          else:
            bstack11111lll11l_opy_[key] = value
      return bstack11111lll11l_opy_
    bstack11111lll11l_opy_ = bstack11111llll11_opy_(config)
    return {
      bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪẮ"): bstack11111l1ll11_opy_,
      bstack11111_opy_ (u"ࠨࡨ࡬ࡲࡦࡲࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫắ"): json.dumps(bstack11111lll11l_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l1llll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠩ࡯ࡳ࡬࠭Ằ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111lllll1_opy_ = os.path.join(log_dir, bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡧࡴࡴࡦࡪࡩࡶࠫằ"))
  if not os.path.exists(bstack11111lllll1_opy_):
    bstack11111llll1l_opy_ = {
      bstack11111_opy_ (u"ࠦ࡮ࡴࡩࡱࡣࡷ࡬ࠧẲ"): str(inipath),
      bstack11111_opy_ (u"ࠧࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠢẳ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack11111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡣࡰࡰࡩ࡭࡬ࡹ࠮࡫ࡵࡲࡲࠬẴ")), bstack11111_opy_ (u"ࠧࡸࠩẵ")) as bstack11111lll111_opy_:
      bstack11111lll111_opy_.write(json.dumps(bstack11111llll1l_opy_))
def bstack11111ll1l11_opy_():
  try:
    bstack11111lllll1_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠨ࡮ࡲ࡫ࠬẶ"), bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨặ"))
    if os.path.exists(bstack11111lllll1_opy_):
      with open(bstack11111lllll1_opy_, bstack11111_opy_ (u"ࠪࡶࠬẸ")) as bstack11111lll111_opy_:
        bstack11111ll1l1l_opy_ = json.load(bstack11111lll111_opy_)
      return bstack11111ll1l1l_opy_.get(bstack11111_opy_ (u"ࠫ࡮ࡴࡩࡱࡣࡷ࡬ࠬẹ"), bstack11111_opy_ (u"ࠬ࠭Ẻ")), bstack11111ll1l1l_opy_.get(bstack11111_opy_ (u"࠭ࡲࡰࡱࡷࡴࡦࡺࡨࠨẻ"), bstack11111_opy_ (u"ࠧࠨẼ"))
  except:
    pass
  return None, None
def bstack11111l1ll1l_opy_():
  try:
    bstack11111lllll1_opy_ = os.path.join(os.getcwd(), bstack11111_opy_ (u"ࠨ࡮ࡲ࡫ࠬẽ"), bstack11111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵ࠱࡮ࡸࡵ࡮ࠨẾ"))
    if os.path.exists(bstack11111lllll1_opy_):
      os.remove(bstack11111lllll1_opy_)
  except:
    pass
def bstack11llllll_opy_(config):
  try:
    from bstack_utils.helper import bstack11l1111l_opy_, bstack11lllll1ll_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111lll1l1_opy_
    if config.get(bstack11111_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬế"), False):
      return
    uuid = os.getenv(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩỀ")) if os.getenv(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪề")) else bstack11l1111l_opy_.get_property(bstack11111_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣỂ"))
    if not uuid or uuid == bstack11111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬể"):
      return
    bstack1111l111111_opy_ = [bstack11111_opy_ (u"ࠨࡴࡨࡵࡺ࡯ࡲࡦ࡯ࡨࡲࡹࡹ࠮ࡵࡺࡷࠫỄ"), bstack11111_opy_ (u"ࠩࡓ࡭ࡵ࡬ࡩ࡭ࡧࠪễ"), bstack11111_opy_ (u"ࠪࡴࡾࡶࡲࡰ࡬ࡨࡧࡹ࠴ࡴࡰ࡯࡯ࠫỆ"), bstack11111lll1l1_opy_, bstack11111ll11l1_opy_]
    bstack11111l1l1l1_opy_, root_path = bstack11111ll1l11_opy_()
    if bstack11111l1l1l1_opy_ != None:
      bstack1111l111111_opy_.append(bstack11111l1l1l1_opy_)
    if root_path != None:
      bstack1111l111111_opy_.append(os.path.join(root_path, bstack11111_opy_ (u"ࠫࡨࡵ࡮ࡧࡶࡨࡷࡹ࠴ࡰࡺࠩệ")))
    bstack1l111lll11_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠲ࡲ࡯ࡨࡵ࠰ࠫỈ") + uuid + bstack11111_opy_ (u"࠭࠮ࡵࡣࡵ࠲࡬ࢀࠧỉ"))
    with tarfile.open(output_file, bstack11111_opy_ (u"ࠢࡸ࠼ࡪࡾࠧỊ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack1111l111111_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111ll1ll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111lll1ll_opy_ = data.encode()
        tarinfo.size = len(bstack11111lll1ll_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111lll1ll_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack11111_opy_ (u"ࠨࡦࡤࡸࡦ࠭ị"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack11111_opy_ (u"ࠩࡵࡦࠬỌ")), bstack11111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰ࡺ࠰࡫ࡿ࡯ࡰࠨọ")),
        bstack11111_opy_ (u"ࠫࡨࡲࡩࡦࡰࡷࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ỏ"): uuid
      }
    )
    bstack11111llllll_opy_ = bstack11lllll1ll_opy_(cli.config, [bstack11111_opy_ (u"ࠧࡧࡰࡪࡵࠥỏ"), bstack11111_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨỐ"), bstack11111_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪࠢố")], bstack11l1l111111_opy_)
    response = requests.post(
      bstack11111_opy_ (u"ࠣࡽࢀ࠳ࡨࡲࡩࡦࡰࡷ࠱ࡱࡵࡧࡴ࠱ࡸࡴࡱࡵࡡࡥࠤỒ").format(bstack11111llllll_opy_),
      data=multipart_data,
      headers={bstack11111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨồ"): multipart_data.content_type},
      auth=(config[bstack11111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬỔ")], config[bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧổ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack11111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶ࡬ࡰࡣࡧࠤࡱࡵࡧࡴ࠼ࠣࠫỖ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡬ࡰࡩࡶ࠾ࠬỗ") + str(e))
  finally:
    try:
      bstack1ll111l11l1_opy_()
      bstack11111l1ll1l_opy_()
    except:
      pass