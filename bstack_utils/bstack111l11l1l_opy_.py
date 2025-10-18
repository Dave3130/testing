# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11llll_opy_, bstack11l11lll1ll_opy_, bstack11l1l1ll1ll_opy_
import tempfile
import json
bstack11111llll1l_opy_ = os.getenv(bstack1l1lll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡋࡤࡌࡉࡍࡇࠥẢ"), None) or os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠧả"))
bstack11111ll1lll_opy_ = os.path.join(bstack1l1lll1_opy_ (u"ࠦࡱࡵࡧࠣẤ"), bstack1l1lll1_opy_ (u"ࠬࡹࡤ࡬࠯ࡦࡰ࡮࠳ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠩấ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l1lll1_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩẦ"),
      datefmt=bstack1l1lll1_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬầ"),
      stream=sys.stdout
    )
  return logger
def bstack1l11lllll1l_opy_():
  bstack11111l1lll1_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡅࡇࡅ࡙ࡌࠨẨ"), bstack1l1lll1_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣẩ"))
  return logging.DEBUG if bstack11111l1lll1_opy_.lower() == bstack1l1lll1_opy_ (u"ࠥࡸࡷࡻࡥࠣẪ") else logging.INFO
def bstack1ll11ll111l_opy_():
  global bstack11111llll1l_opy_
  if os.path.exists(bstack11111llll1l_opy_):
    os.remove(bstack11111llll1l_opy_)
  if os.path.exists(bstack11111ll1lll_opy_):
    os.remove(bstack11111ll1lll_opy_)
def bstack1l1l11l111_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l1llll_opy_ = log_level
  if bstack1l1lll1_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ẫ") in config and config[bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧẬ")] in bstack11l11lll1ll_opy_:
    bstack11111l1llll_opy_ = bstack11l11lll1ll_opy_[config[bstack1l1lll1_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨậ")]]
  if config.get(bstack1l1lll1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩẮ"), False):
    logging.getLogger().setLevel(bstack11111l1llll_opy_)
    return bstack11111l1llll_opy_
  global bstack11111llll1l_opy_
  bstack1l1l11l111_opy_()
  bstack11111l1ll11_opy_ = logging.Formatter(
    fmt=bstack1l1lll1_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫắ"),
    datefmt=bstack1l1lll1_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧẰ"),
  )
  bstack11111l1l1ll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111llll1l_opy_)
  file_handler.setFormatter(bstack11111l1ll11_opy_)
  bstack11111l1l1ll_opy_.setFormatter(bstack11111l1ll11_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111l1l1ll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l1lll1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬằ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111l1l1ll_opy_.setLevel(bstack11111l1llll_opy_)
  logging.getLogger().addHandler(bstack11111l1l1ll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l1llll_opy_
def bstack11111lll1ll_opy_(config):
  try:
    bstack11111ll1ll1_opy_ = set(bstack11l1l1ll1ll_opy_)
    bstack11111ll11l1_opy_ = bstack1l1lll1_opy_ (u"ࠫࠬẲ")
    with open(bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨẳ")) as bstack11111lll111_opy_:
      bstack11111ll11ll_opy_ = bstack11111lll111_opy_.read()
      bstack11111ll11l1_opy_ = re.sub(bstack1l1lll1_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠤ࠰࠭ࠨࡡࡴࠧẴ"), bstack1l1lll1_opy_ (u"ࠧࠨẵ"), bstack11111ll11ll_opy_, flags=re.M)
      bstack11111ll11l1_opy_ = re.sub(
        bstack1l1lll1_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠫࠫẶ") + bstack1l1lll1_opy_ (u"ࠩࡿࠫặ").join(bstack11111ll1ll1_opy_) + bstack1l1lll1_opy_ (u"ࠪ࠭࠳࠰ࠤࠨẸ"),
        bstack1l1lll1_opy_ (u"ࡶࠬࡢ࠲࠻ࠢ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ẹ"),
        bstack11111ll11l1_opy_, flags=re.M | re.I
      )
    def bstack11111l1l11l_opy_(dic):
      bstack11111llllll_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111ll1ll1_opy_:
          bstack11111llllll_opy_[key] = bstack1l1lll1_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩẺ")
        else:
          if isinstance(value, dict):
            bstack11111llllll_opy_[key] = bstack11111l1l11l_opy_(value)
          else:
            bstack11111llllll_opy_[key] = value
      return bstack11111llllll_opy_
    bstack11111llllll_opy_ = bstack11111l1l11l_opy_(config)
    return {
      bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩẻ"): bstack11111ll11l1_opy_,
      bstack1l1lll1_opy_ (u"ࠧࡧ࡫ࡱࡥࡱࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪẼ"): json.dumps(bstack11111llllll_opy_)
    }
  except Exception as e:
    return {}
def bstack11111lll11l_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1l1lll1_opy_ (u"ࠨ࡮ࡲ࡫ࠬẽ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111ll1l1l_opy_ = os.path.join(log_dir, bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵࠪẾ"))
  if not os.path.exists(bstack11111ll1l1l_opy_):
    bstack11111l1l1l1_opy_ = {
      bstack1l1lll1_opy_ (u"ࠥ࡭ࡳ࡯ࡰࡢࡶ࡫ࠦế"): str(inipath),
      bstack1l1lll1_opy_ (u"ࠦࡷࡵ࡯ࡵࡲࡤࡸ࡭ࠨỀ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫề")), bstack1l1lll1_opy_ (u"࠭ࡷࠨỂ")) as bstack1111l111111_opy_:
      bstack1111l111111_opy_.write(json.dumps(bstack11111l1l1l1_opy_))
def bstack11111ll111l_opy_():
  try:
    bstack11111ll1l1l_opy_ = os.path.join(os.getcwd(), bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡪࠫể"), bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧỄ"))
    if os.path.exists(bstack11111ll1l1l_opy_):
      with open(bstack11111ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠩࡵࠫễ")) as bstack1111l111111_opy_:
        bstack11111ll1l11_opy_ = json.load(bstack1111l111111_opy_)
      return bstack11111ll1l11_opy_.get(bstack1l1lll1_opy_ (u"ࠪ࡭ࡳ࡯ࡰࡢࡶ࡫ࠫỆ"), bstack1l1lll1_opy_ (u"ࠫࠬệ")), bstack11111ll1l11_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠧỈ"), bstack1l1lll1_opy_ (u"࠭ࠧỉ"))
  except:
    pass
  return None, None
def bstack11111lll1l1_opy_():
  try:
    bstack11111ll1l1l_opy_ = os.path.join(os.getcwd(), bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡪࠫỊ"), bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧị"))
    if os.path.exists(bstack11111ll1l1l_opy_):
      os.remove(bstack11111ll1l1l_opy_)
  except:
    pass
def bstack1l1l1111_opy_(config):
  try:
    from bstack_utils.helper import bstack1111111l_opy_, bstack11l11ll11l_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111llll1l_opy_
    if config.get(bstack1l1lll1_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫỌ"), False):
      return
    uuid = os.getenv(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨọ")) if os.getenv(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩỎ")) else bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢỏ"))
    if not uuid or uuid == bstack1l1lll1_opy_ (u"࠭࡮ࡶ࡮࡯ࠫỐ"):
      return
    bstack11111l1ll1l_opy_ = [bstack1l1lll1_opy_ (u"ࠧࡳࡧࡴࡹ࡮ࡸࡥ࡮ࡧࡱࡸࡸ࠴ࡴࡹࡶࠪố"), bstack1l1lll1_opy_ (u"ࠨࡒ࡬ࡴ࡫࡯࡬ࡦࠩỒ"), bstack1l1lll1_opy_ (u"ࠩࡳࡽࡵࡸ࡯࡫ࡧࡦࡸ࠳ࡺ࡯࡮࡮ࠪồ"), bstack11111llll1l_opy_, bstack11111ll1lll_opy_]
    bstack11111llll11_opy_, root_path = bstack11111ll111l_opy_()
    if bstack11111llll11_opy_ != None:
      bstack11111l1ll1l_opy_.append(bstack11111llll11_opy_)
    if root_path != None:
      bstack11111l1ll1l_opy_.append(os.path.join(root_path, bstack1l1lll1_opy_ (u"ࠪࡧࡴࡴࡦࡵࡧࡶࡸ࠳ࡶࡹࠨỔ")))
    bstack1l1l11l111_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡱࡵࡧࡴ࠯ࠪổ") + uuid + bstack1l1lll1_opy_ (u"ࠬ࠴ࡴࡢࡴ࠱࡫ࡿ࠭Ỗ"))
    with tarfile.open(output_file, bstack1l1lll1_opy_ (u"ࠨࡷ࠻ࡩࡽࠦỗ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1ll1l_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111lll1ll_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111lllll1_opy_ = data.encode()
        tarinfo.size = len(bstack11111lllll1_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111lllll1_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1l1lll1_opy_ (u"ࠧࡥࡣࡷࡥࠬỘ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l1lll1_opy_ (u"ࠨࡴࡥࠫộ")), bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࠯ࡪࡾ࡮ࡶࠧỚ")),
        bstack1l1lll1_opy_ (u"ࠪࡧࡱ࡯ࡥ࡯ࡶࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬớ"): uuid
      }
    )
    bstack11111ll1111_opy_ = bstack11l11ll11l_opy_(cli.config, [bstack1l1lll1_opy_ (u"ࠦࡦࡶࡩࡴࠤỜ"), bstack1l1lll1_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧờ"), bstack1l1lll1_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩࠨỞ")], bstack11l1l11llll_opy_)
    response = requests.post(
      bstack1l1lll1_opy_ (u"ࠢࡼࡿ࠲ࡧࡱ࡯ࡥ࡯ࡶ࠰ࡰࡴ࡭ࡳ࠰ࡷࡳࡰࡴࡧࡤࠣở").format(bstack11111ll1111_opy_),
      data=multipart_data,
      headers={bstack1l1lll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧỠ"): multipart_data.content_type},
      auth=(config[bstack1l1lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫỡ")], config[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭Ợ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡹࡵࡲ࡯ࡢࡦࠣࡰࡴ࡭ࡳ࠻ࠢࠪợ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l1lll1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵ࠽ࠫỤ") + str(e))
  finally:
    try:
      bstack1ll11ll111l_opy_()
      bstack11111lll1l1_opy_()
    except:
      pass